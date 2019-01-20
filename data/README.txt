Airport and Destination Data
****************************

- airports.csv.headers
- airports.csv
- destinations.csv.headers
- destinations.csv

The airport and destination data was derived from the OpenFlights Airports Database (https://openflights.org/data.html). The data is available on GitHub (https://github.com/jpatokal/openflights/blob/master/data/airports.dat) under the Open Database License (https://openflights.org/data.html#license).

There are separate files for the actual data and headers. 

The file airports.csv contains a fairly complete list of commercial airports with these fields:

- iata_code # International Air Transport Association (IATA) code
- lat       # latitude (postive numbers: degrees North, negative numbers: degrees South) 
- long      # longitude (postive numbers: degrees East, negative numbers: degrees West) 

The file destinations.csv contains a selection of cities, mostly popular travel destinations in Western Europe and North America. Fields:

- city      # English name of city
- country   # English name of country
- iata_code # International Air Transport Association (IATA) code of the main airport of the city
- lat       # latitude of the airport (postive numbers: degrees North, negative numbers: degrees South) 
- long      # longitude of the airport (postive numbers: degrees East, negative numbers: degrees West) 


Weather Data
************

- weather_conditions.csv

Fields:

- iata_code # International Air Transport Association (IATA) code of the main airport of the city
- month     # English name of month
- min_temperature_celsius # average minimum temperature over the last twelve years in degrees Celsius
- max_temperature_celsius # average (or absolute?) maximum temperature over the last twelve years in degrees Celsius
- daily_precipitation_mm  # average daily rainfall/precipitation over the last twelve years in millimeters

Accurate weather data can be obtained from World Weather Online (https://www.worldweatheronline.com), using the Local Weather API (see section below). 

The script get_weather_data.py can be used for this purpose (minus the randomization). The script explore_weather_data.py can be used for exploration of the API. Both scripts require an API key.

The file weather_conditions.csv does not contain data as obtained from World Weather Online, but data with random modifications. This data is only intended for demos of the "Alternative Destinations" web service and is not fit for any practical purpose.  

When using weather data obtained from World Weather Online the following terms and conditions apply (https://www.worldweatheronline.com/developer/api/api-t-and-c.aspx):

"World Weather Online grants you the right to access, use, and view the standard (free) Services, together with any Premium Services for which you have subscribed and agreed to pay the applicable subscription fees, You may access, view and make copies of the data in the API for your personal or commercial use, including making the data in the API available in online and/or mobile applications/services (a single API key/subscription may be used in respect of one online or mobile application/service only – e.g. iSuite online) which are, as applicable, sold or resold by you or your group companies or other third parties authorised by you (‘Representatives’). If you are Free API user then for all uses of the data, you will credit World Weather Online by name or brand logo as the source of the data. You may not transfer your access privileges or disclose your password to any third party. World Weather Online reserves the right to modify or terminate any of the Services at any time. You agree not to sell our weather data to any third party. As a condition of your use of the Services, you warrant to World Weather Online that you will not use the Services for any purpose that is unlawful or prohibited by these Terms and Conditions. If you violate any of these Terms and Conditions, your authorization to use the Services automatically terminates and you must immediately destroy any downloaded or printed materials."

Weather data for airports can also be obtained from the Iowa Environmental Mesonet website of Iowa State University (https://mesonet.agron.iastate.edu/request/download.phtml?network=IN__ASOS). For accessing the Iowa Environmental Mesonet data, try one of the following:

- https://github.com/akrherz/iem/blob/master/scripts/asos/iem_scraper_example.py
- https://github.com/realmiketalbot/Public/blob/master/iem_scraper_example.r
- http://ropensci.github.io/riem/


World Weather Online API
************************

https://www.worldweatheronline.com/developer/api/docs/local-city-town-weather-api.aspx

"The Premium Local Weather REST API method allows you to access current weather conditions and the next 15 days of accurate and reliable weather forecast. The Local Weather API returns weather elements such as temperature, precipitation (rainfall), weather description, weather icon and wind speed.

You can also use this method to get monthly climate average data for a specified location, averaged over the last 12 years. Available weather elements include average minimum and maximum temperatures, absolute minimum and maximum temperatures, average rainfall, and average number of dry, snow, and fog days."


Example URL for Monthly Average Data
------------------------------------

https://api.worldweatheronline.com/premium/v1/weather.ashx?key=1a2b3c&q=LHR&date=2020-01-01&cc=no&mca=yes&format=json

(Note: If date is so far in future that weather forecast is not available only average data is returned.)


Base URL
--------

https://api.worldweatheronline.com/premium/v1/weather.ashx


Query Parameters (Selection)
----------------------------

q=LHR             # Undocumented feature: query using IATA codes.
isDayTime         # Adds yes for day and no for night time period. Note: This parameter only works with 3 hourly, 6 hourly or 12 hourly intervals.
num_of_days=1     # Forecast only for one day.
date=2019-01-20   # Date weather forecast is requested for. If date is so far in future that weather forecast is not available only average data is returned.
cc=no             # Whether to return current weather conditions output.
mca=yes           # Whether to return monthly climate average data.
tp=12             # Specifies the weather forecast time interval in hours. Options are: 1 hour, 3 hourly, 6 hourly, 12 hourly (day/night) or 24 hourly (day average).
format=json       # Format of returned data.
key=...           # API key

