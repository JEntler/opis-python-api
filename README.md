# OPIS RealtimePriceService Web Service Python API

Easy-to-use Python interface for the OPIS RealtimePriceService Web Service

## Getting Started

Setup is simple:

* Add your customer token to *credentials.py*
* Import desired function from *opis.py*
* Enjoy the dictionary output!

### Quickstart

```
from opis import authenticate, getzipcoderesults
import credentials

user_ticket = authenticate(credentials.CUSTOMER_TOKEN)

results = getzipcoderesults(user_ticket, zip="90048")
```

## Sample Output

The following fields will be returned for all web service methods:

```
{
  "station_1": 
    {
      "address_1": "7900 BEVERLY BLVD",
      "address_2": None,
      "brand_name": "United",
      "city": "Los Angeles",
      "diesel_date": None,
      "diesel_id": "1",
      "diesel_price": None,
      "distance_to_station": None,
      "latitude": "34.0760532131",
      "longitude": "-118.3614844154",
      "midgrade_date": "2017-06-27T18:43:46.627-04:00",
      "midgrade_id": "4",
      "midgrade_price": "3.09900000",
      "phone": "(323)935-2322",
      "premium_date": "2017-06-27T18:43:46.627-04:00",
      "premium_id": "5",
      "premium_price": "3.29900000",
      "state": "CA",
      "station_id": "314688",
      "station_name": "UNITED OIL-APRO #2",
      "unleaded_date": "2017-06-27T18:43:46.627-04:00",
      "unleaded_id": "3",
      "unleaded_price": "2.99900000",
      "zip": "90048"
   }
}
```

## Running the tests

Configure service-area variables within *tests.py* and run:

```
python tests.py
```
:heavy_check_mark:

## Extended Example

Easily find the average price of gas in a ZIP Code:

```
from opis import authenticate, getzipcoderesults
import credentials

user_ticket = authenticate(credentials.CUSTOMER_TOKEN)

results = getzipcoderesults(user_ticket, 90048)

unleaded_prices = []
for i, result in enumerate(results, start=1):
    unleaded_prices.append(float(results['station_{}'.format(i)]['unleaded_price']))

average_price = sum(unleaded_prices) / len(unleaded_prices)

print(average_price)
```

## Available Methods

[Authenticate](https://services.opisnet.com/RealtimePriceService/RealtimePriceServicePlus.asmx?op=Authenticate)
```
 authenticate(customer_token)
```
[GetCityStateSortedResults](https://services.opisnet.com/RealtimePriceService/RealtimePriceServicePlus.asmx?op=GetCityStateSortedResults)
```
 getcitystatesortedresults(user_ticket, city, state, sort_product)
```
[GetLatLongResults](https://services.opisnet.com/RealtimePriceService/RealtimePriceServicePlus.asmx?op=GetLatLongResults)
```
 getlatlongresults(user_ticket, lat, long)
```
[GetLatLongSortedResults](https://services.opisnet.com/RealtimePriceService/RealtimePriceServicePlus.asmx?op=GetLatLongSortedResults)
```
 getlatlongsortedresults(user_ticket, lat, long, sort_product)
```
[GetLatLongSortedWithDistanceResults](https://services.opisnet.com/RealtimePriceService/RealtimePriceServicePlus.asmx?op=GetLatLongSortedWithDistanceResults)
```
 getlatlongsortedwithdistanceresults(user_ticket, sort_product, filter_distance, 
                                     distance, lat, long, user_lat, user_long)
```
[GetZipCodeResults](https://services.opisnet.com/RealtimePriceService/RealtimePriceServicePlus.asmx?op=GetZipCodeResults)
```
 getzipcoderesults(user_ticket, zip)
```
[GetZipCodeSortedResults](https://services.opisnet.com/RealtimePriceService/RealtimePriceServicePlus.asmx?op=GetZipCodeSortedResults)
```
  getzipcodesortedresults(user_ticket, zip, sort_product)
```

## Dependencies :clap:

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
* [Requests](http://docs.python-requests.org/en/master/)