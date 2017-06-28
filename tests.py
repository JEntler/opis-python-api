import unittest

import credentials
from opis import (
	authenticate, getzipcoderesults, getlatlongresults,
	getzipcodesortedresults, getlatlongsortedresults,
	getcitystatesortedresults, getlatlongsortedwithdistanceresults
)


class TestOpisMethods(unittest.TestCase):
	def setUp(self):
		self.customer_token = credentials.CUSTOMER_TOKEN
		self.user_ticket = authenticate(self.customer_token)
		self.city = "Los Angeles"
		self.state = "CA"
		self.sort_product = "Unleaded"
		self.lat = "34.040310"
		self.long = "-118.232804"
		self.distance = "10"
		self.filter_distance = "False"
		self.user_lat = "34.040310"
		self.user_long = "-118.232804"
		self.zip = "90048"

	def test_authenticate(self):
		self.assertTrue(self.user_ticket)

	def test_getcitystatesortedresults(self):
		output = getcitystatesortedresults(
			self.user_ticket, self.city, self.state, self.sort_product
		)
		print(output, "\n")
		self.assertTrue(output)

	def test_getlatlongresults(self):
		output = getlatlongresults(self.user_ticket, self.lat, self.long)
		print(output, "\n")
		self.assertTrue(output)

	def test_getlatlongsortedresults(self):
		output = getlatlongsortedresults(
			self.user_ticket, self.lat, self.long, self.sort_product
		)
		print(output, "\n")
		self.assertTrue(output)

	def test_getlatlongsortedwithdistanceresults(self):
		output = getlatlongsortedwithdistanceresults(
			self.user_ticket, self.lat, self.long, self.sort_product,
			self.distance, self.filter_distance,
			self.user_lat, self.user_long
		)
		print(output, "\n")
		self.assertTrue(output)

	def test_getzipcoderesults(self):
		output = getzipcoderesults(self.user_ticket, self.zip)
		print(output, "\n")
		self.assertTrue(output)

	def test_getzipcodesortedresults(self):
		output = getzipcodesortedresults(
			self.user_ticket, self.zip, self.sort_product
		)
		print(output, "\n")
		self.assertTrue(output)


if __name__ == '__main__':
	unittest.main()
