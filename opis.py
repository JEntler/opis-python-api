import requests
from bs4 import BeautifulSoup

import constants


def authenticate(customer_token):
	payload = {'CustomerToken': customer_token}
	url = constants.AUTHENTICATE_URL
	r = requests.post(url, data=payload)
	soup = BeautifulSoup(r.text, "xml")
	user_ticket = soup.string
	return user_ticket


def getcitystatesortedresults(user_ticket, city, state, sort_product):
	payload = {
		'UserTicket': user_ticket, 'City': city, 'State': state,
		'SortByProduct': sort_product
	}
	url = constants.GET_CITY_STATE_SORTED_RESULTS_URL
	r = requests.post(url, data=payload)
	return to_dict(r)


def getlatlongresults(user_ticket, lat, long):
	payload = {'UserTicket': user_ticket, 'Latitude': lat, 'Longitude': long}
	url = constants.GET_LAT_LONG_RESULTS_URL
	r = requests.post(url, data=payload)
	return to_dict(r)


def getlatlongsortedresults(user_ticket, lat, long, sort_product):
	payload = {
		'UserTicket': user_ticket, 'Latitude': lat, 'Longitude': long,
		'SortByProduct': sort_product
	}
	url = constants.GET_LAT_LONG_SORTED_RESULTS_URL
	r = requests.post(url, data=payload)
	return to_dict(r)


def getlatlongsortedwithdistanceresults(user_ticket, lat, long, sort_product, distance, filter_distance, user_lat, user_long):
	payload = {
		'UserTicket': user_ticket, 'Latitude': lat,
		'Longitude': long, 'SortByProduct': sort_product,
		'distance': distance, 'isFilteredByDistance': filter_distance,
		'UserLatitude': user_lat, 'UserLongitude': user_long
	}
	url = constants.GET_LAT_LONG_SORTED_WITH_DISTANCE_RESULTS_URL
	r = requests.post(url, data=payload)
	return to_dict(r, tag='StationPricesByLatLongMultiPlus')


def getzipcoderesults(user_ticket, zip):
	payload = {'UserTicket': user_ticket, 'ZipCode': zip}
	url = constants.GET_ZIPCODE_RESULTS_URL
	r = requests.post(url, data=payload)
	return to_dict(r)


def getzipcodesortedresults(user_ticket, zip, sort_product):
	payload = {
		'UserTicket': user_ticket, 'ZipCode': zip,
		'SortByProduct': sort_product
	}
	url = constants.GET_ZIPCODE_SORTED_RESULTS_URL
	r = requests.post(url, data=payload)
	return to_dict(r)


def to_dict(r, **kwarg):
	soup = BeautifulSoup(r.text, "xml")
	output = {}
	output["stations"] = {}
	if ('tag' in kwarg):
		tag = kwarg['tag']
	else:
		tag = "StationPricesMultiPlus"
	for i, station in enumerate(soup.find_all(tag), start=1):
		station_results = {}
		for field in constants.fields:
			try:
				station_results[field[0]] = station.find(field[1]).string
			except (AttributeError):
				station_results[field[0]] = None
		output["stations"]["station_{}".format(i)] = station_results
	output["count"] = len(output["stations"])
	return output
