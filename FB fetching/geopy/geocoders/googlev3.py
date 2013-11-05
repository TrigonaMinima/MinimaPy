"""
:class:`.GoogleV3` is the Google Maps V3 geocoder.
"""

from warnings import warn

import base64
import hashlib
import hmac
from geopy.compat import urlencode
from geopy.geocoders.base import Geocoder, DEFAULT_TIMEOUT, DEFAULT_SCHEME
from geopy.util import logger
from geopy.exc import GeocoderQueryError, GeocoderQuotaExceeded, ConfigurationError


class GoogleV3(Geocoder):
    """
    Geocoder using the Google Maps v3 API. Documentation at:
        https://developers.google.com/maps/documentation/geocoding/
    """

    def __init__(self, domain='maps.googleapis.com', scheme=DEFAULT_SCHEME, # pylint: disable=R0913
                 client_id=None, secret_key=None, timeout=DEFAULT_TIMEOUT,
                 proxies=None, protocol=None):
        """
        Initialize a customized Google geocoder.

        API authentication is only required for Google Maps Premier customers.

        :param string domain: Should be the localized Google Maps domain to
            connect to. The default is 'maps.google.com', but if you're
            geocoding address in the UK (for example), you may want to set it
            to 'maps.google.co.uk' to properly bias results.

        :param string scheme: Use 'https' or 'http' as the API URL's scheme.
            Default is https. Note that SSL connections' certificates are not
            verified.

            .. versionadded:: 0.97

        :param string protocol: Deprecated version of `scheme` argument.
            Override scheme, if present.

        :param string client_id: If using premier, the account client id.

        :param string secret_key: If using premier, the account secret key.

        :param dict proxies: If specified, routes this geocoder's requests
            through the specified proxy. E.g., {"https": "192.0.2.0"}. For
            more information, see documentation on
            :class:`urllib2.ProxyHandler`.

            .. versionadded:: 0.96
        """
        if protocol:
            warn('protocol argument is deprecated in favor of scheme, to be'
                'removed in 0.98')
        scheme = protocol or scheme
        super(GoogleV3, self).__init__(scheme=scheme, timeout=timeout, proxies=proxies)
        if client_id and not secret_key:
            raise ConfigurationError('Must provide secret_key with client_id.')
        if secret_key and not client_id:
            raise ConfigurationError('Must provide client_id with secret_key.')

        self.domain = domain.strip('/')
        self.scheme = scheme
        self.doc = {}

        if client_id and secret_key:
            self.premier = True
            self.client_id = client_id
            self.secret_key = secret_key
        else:
            self.premier = False
            self.client_id = None
            self.secret_key = None

    def _get_url(self, params):
        '''Returns a standard geocoding api url.'''
        return '%(scheme)s://%(domain)s/maps/api/geocode/json?%(params)s' % (
            {'scheme': self.scheme, 'domain': self.domain, 'params': urlencode(params)})

    def _get_signed_url(self, params):
        '''Returns a Premier account signed url.'''
        params['client'] = self.client_id
        url_params = {
            'scheme': self.scheme,
            'domain': self.domain,
            'params': urlencode(params)
        }
        secret = base64.urlsafe_b64decode(self.secret_key)
        url_params['url_part'] = (
            '/maps/api/geocode/json?%(params)s' % url_params
        )
        signature = hmac.new(secret, url_params['url_part'], hashlib.sha1)
        url_params['signature'] = base64.urlsafe_b64encode(signature.digest())

        return ('%(scheme)s://%(domain)s%(url_part)s'
                '&signature=%(signature)s' % url_params)

    def geocode(self, query, bounds=None, region=None, # pylint: disable=W0221,R0913
                language=None, sensor=False, exactly_one=True, timeout=None):
        """
        Geocode a location query.

        :param string query: The address or query you wish to geocode.

        :param bounds: The bounding box of the viewport within which
            to bias geocode results more prominently.
        :type bounds: list or tuple

        :param string region: The region code, specified as a ccTLD
            ("top-level domain") two-character value.

        :param string language: The language in which to return results.

        :param bool sensor: Whether the geocoding request comes from a
            device with a location sensor.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call only,
            the value set during the geocoder's initialization.

            .. versionadded:: 0.97
        """
        params = {
            'address': self.format_string % query,
            'sensor': str(sensor).lower()
        }
        if bounds:
            params['bounds'] = bounds
        if region:
            params['region'] = region
        if language:
            params['language'] = language

        if not self.premier:
            url = self._get_url(params)
        else:
            url = self._get_signed_url(params)

        logger.debug("%s.geocode: %s", self.__class__.__name__, url)
        return self._parse_json(self._call_geocoder(url, timeout=timeout), exactly_one)

    def reverse(self, query, language=None, # pylint: disable=W0221,R0913
                    sensor=False, exactly_one=False, timeout=None):
        """
        Given a point, find an address.

        :param query: The coordinates for which you wish to obtain the
            closest human-readable addresses.
        :type query: :class:`geopy.point.Point`, list or tuple of (latitude,
            longitude), or string as "%(latitude)s, %(longitude)s"

        :param string language: The language in which to return results.

        :param boolean sensor: Whether the geocoding request comes from a
            device with a location sensor.

        :param boolean exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception.

            .. versionadded:: 0.97
        """
        params = {
            'latlng': self._coerce_point_to_string(query),
            'sensor': str(sensor).lower()
        }
        if language:
            params['language'] = language

        if not self.premier:
            url = self._get_url(params)
        else:
            url = self._get_signed_url(params)

        logger.debug("%s.reverse: %s", self.__class__.__name__, url)
        return self._parse_json(self._call_geocoder(url, timeout=timeout), exactly_one)

    def _parse_json(self, page, exactly_one=True):
        '''Returns location, (latitude, longitude) from json feed.'''

        places = page.get('results', [])
        if not len(places):
            self._check_status(page.get('status'))
            return None

        def parse_place(place):
            '''Get the location, lat, lng from a single json place.'''
            location = place.get('formatted_address')
            latitude = place['geometry']['location']['lat']
            longitude = place['geometry']['location']['lng']
            return (location, (latitude, longitude))

        if exactly_one:
            return parse_place(places[0])
        else:
            return [parse_place(place) for place in places]

    @staticmethod
    def _check_status(status):
        """
        Validates error statuses.
        """
        if status == 'ZERO_RESULTS':
            # When there are no results, just return.
            return
        if status == 'OVER_QUERY_LIMIT':
            raise GeocoderQuotaExceeded(
                'The given key has gone over the requests limit in the 24'
                ' hour period or has submitted too many requests in too'
                ' short a period of time.'
            )
        elif status == 'REQUEST_DENIED':
            raise GeocoderQueryError(
                'Your request was denied.'
            )
        elif status == 'INVALID_REQUEST':
            raise GeocoderQueryError('Probably missing address or latlng.')
        else:
            raise GeocoderQueryError('Unknown error.')

