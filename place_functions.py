import googlemaps
from googlemaps import geolocation
from googlemaps import places
from datetime import datetime

# ASAP -- Store this in an environment variable for security reasons
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



# Function called upon creation of a new story. 
# Returns a users Story as a list a dict inside for event one
def initialize_story(start_location=None):
	story = list()

	if start_location:
		start_loc = gmaps.geocode(start_location)
	else: 
		start_loc = geolocation.geolocate(client=gmaps)

	story.append(start_loc)
	return story


# Function called upon selection of previous event.
# Returns dict with nearby events
# One issue -- Google Maps API doesn't want developers to scrape large amounts of data. Capped at 60 Search queries. 
def list_nearby_events(curr_location=None, search_radius=None, event_type=None):

	if event_type:
		nearby_gmaps_results = places.places_nearby(client=gmaps, location=curr_location, keyword="Food", radius=search_radius)
	else:
		nearby_gmaps_results = places.places_nearby(client=gmaps, location=curr_location, keyword="Food", radius=search_radius)

	# Convert google maps into "Story" compatible data type
	if nearby_gmaps_results:
		nearby_events = nearby_gmaps_results['results']
		return nearby_events

# Temp function. List names for object returned by list_nearby_events
def list_nearby_event_names(data):
	for i in range(len(data)):
		print(data[i]['name'])



# REMOVE THIS STUFF
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
	story = initialize_story()


	#lat_lng = story[0]['location']
	lat_lng = [37.8898303, -122.06701120000002] #This is the lat and longitude of a house in Walnut Creek
	places_dict = list_nearby_events(curr_location=lat_lng, search_radius=1000)

	list_nearby_event_names(places_dict)

	# Get directions from one point to another
	# now = datetime.now()
	# directions_results = gmaps.directions("161 Camelia Lane", "UCLA", mode="transit", departure_time=now)
	# print(directions_results)