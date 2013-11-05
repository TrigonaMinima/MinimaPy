import facebook as fb
from geopy import geocoders
import simplekml

token = 'access token'

graph = fb.GraphAPI(token)
maps = geocoders.GoogleV3()
kml = simplekml.Kml()

friends = graph.get_connections("me", "friends")

for friend in friends['data']:
	p = graph.get_object(friend['id'])
	if 'hometown' in p :
		place, (lat, lng) = maps.geocode(p['hometown']['name'])
		kml.newpoint(coords=[(lng,lat)])

kml.save("friends_hometown.kml")
