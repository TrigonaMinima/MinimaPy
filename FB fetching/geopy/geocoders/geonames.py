"""
:class:`GeoNames` geocoder.
"""

from geopy.compat import urlencode

from geopy.geocoders.base import Geocoder, DEFAULT_TIMEOUT
from geopy.util import logger
from geopy.exc import GeocoderInsufficientPrivileges, GeocoderError, \
    ConfigurationError


class GeoNames(Geocoder): # pylint: disable=W0223
    """
    GeoNames geocoder, documentation at:
        http://www.geonames.org/export/geonames-search.html

    Reverse geocoding also available, but not yet implemented. Documentation at:
        http://www.geonames.org/maps/us-reverse-geocoder.html
    """

    def __init__(self, country_bias=None, username=None, timeout=DEFAULT_TIMEOUT, proxies=None):
        """
        :param string country_bias:

        :param string username:

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception.

            .. versionadded:: 0.97

        :param dict proxies: If specified, routes this geocoder's requests
            through the specified proxy. E.g., {"https": "192.0.2.0"}. For
            more information, see documentation on
            :class:`urllib2.ProxyHandler`.

            .. versionadded:: 0.96

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception.

            .. versionadded:: 0.97
        """
        super(GeoNames, self).__init__(scheme='http', timeout=timeout, proxies=proxies)
        if username == None:
            raise ConfigurationError(
                'No username given, required for api access.  If you do not '
                'have a GeoNames username, sign up here: '
                'http://www.geonames.org/login'
            )
        self.username = username
        self.country_bias = country_bias
        self.api = "%s://api.geonames.org/searchJSON" % self.scheme

    def geocode(self, query, exactly_one=True, timeout=None): # pylint: disable=W0221
        """
        Geocode a location query.

        :param string query: The address or query you wish to geocode.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call only,
            the value set during the geocoder's initialization.

            .. versionadded:: 0.97
        """
        params = {
            'q': query,
            'username': self.username
        }
        if self.country_bias:
            params['countryBias'] = self.country_bias
        if exactly_one is True:
            params['maxRows'] = 1
        url = "?".join((self.api, urlencode(params)))
        logger.debug("%s.geocode: %s", self.__class__.__name__, url)
        return self._parse_json(self._call_geocoder(url, timeout=timeout), exactly_one)

    def _parse_json(self, doc, exactly_one):
        """
        Parse JSON response body.
        """
        places = doc.get('geonames', [])
        err = doc.get('status', None)
        if err and 'message' in err:
            if err['message'].startswith("user account not enabled to use"):
                raise GeocoderInsufficientPrivileges(err['message'])
            else:
                raise GeocoderError(err['message'])
        if not len(places):
            return None

        def parse_code(place):
            latitude = place.get('lat', None)
            longitude = place.get('lng', None)
            if latitude and longitude:
                latitude = float(latitude)
                longitude = float(longitude)
            else:
                return None

            placename = place.get('name')
            state = place.get('adminCode1', None)
            country = place.get('countryCode', None)

            location = ', '.join(
                [x for x in [placename, state, country] if x]
            )

            return (location, (latitude, longitude))

        if exactly_one:
            return parse_code(places[0])
        else:
            return [parse_code(place) for place in places]
