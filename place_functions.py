import googlemaps
from googlemaps import geolocation
from googlemaps import places
from datetime import datetime

# Store this in an environment variable
gmaps = googlemaps.Client(key='AIzaSyC94G_D29MnwKOepVNsTOqfu99PYtlcuAU')

# Stories are lists of events (stored in dicts)
# Stories should be returned to 
example_story = [
	{
		"Event Title": "Bowling",
		"Category": "Activity",
		"Event location": "1234 Haashole Rd, Goober Germany, 91111",
		"Start Time": "4:00 PM",
		"End Time": "5:00 PM",
	},
	{
		"Event Title": "Dinner",
		"Cateogry": "Food",
		"Event location": "111 Camelia Lane, Walnut Creek, CA 94595",
		"Start Time": "6:00 PM",
		"End Time": "7:00 PM",
	}
]

class CreateStory():
	def __init__(self, start_loc=None, end_loc=None, story_duration=None, story_budget=None):
		self.story = list()

	def create_start_event(self, location=None):
		if location:
			start_loc = gmaps.geocode(location)
		else:
			start_loc = geolocation.geolocate(client=gmaps)
		
		if start_loc:
			self.story.append(start_loc)

	# Remove this function. Add class inheritance for "places_nearby" ?
	def list_nearby_places(self, location, category):
		places_dict = places.places_nearby(location, category)
		return places_dict

	def append_event(self, event):
		self.story.append(event)

	def choose_category(self, previous_event, current_time):
		return None

	def allocate_time(self, event):
		return None

# Parameters for Google API place_nearby function
'''
def places_nearby(client, location=None, radius=None, keyword=None,
                  language=None, min_price=None, max_price=None, name=None,
                  open_now=False, rank_by=None, type=None, page_token=None):
'''


if __name__ == "__main__":
	user1_story = CreateStory()
	user1_story.create_start_event()
	event_one = user1_story.story[0]
	print(event_one)


	# Get directions from one point to another
	# now = datetime.now()
4directions_results = gmaps.directions("161 Camelia Lane", "UCLA", mode="transit", departure_time=now)
# print(directions_results)
1.