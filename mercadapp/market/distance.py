from django.conf import settings
import googlemaps

class Distance(object):

	def get_distance_between(self, origin, destination):
		gmaps = googlemaps.Client(key=settings.GMAPS_API_KEY)
		result = gmaps.distance_matrix(origin, destination)
		distance = result['rows'][0]['elements'][0]['distance']['value'] / 1000.0
		return distance