import facebook
from geopy import geocoders
import simplekml

token = 'access token'

graph = facebook.GraphAPI(token)
maps = geocoders.GoogleV3()
kml = simplekml.Kml()

groups = graph.get_connections("me", "groups")
for grp in groups['data']:
	if grp['name'] == 'group name':
		group_members = graph.get_connections(grp['id'], "members")
print group_members['data']

hometown_fetched = []
for mem in group_members['data']:
	p = graph.get_object(mem['id'])
	if 'hometown' in p :
		hometown_fetched.append(p['hometown']['name'])
print hometown_fetched

for place in hometown_fetched:
	place, (lat, lng) = maps.geocode(place)
	kml.newpoint(coords=[(lng, lat)])

kml.save("group_members.kml")
