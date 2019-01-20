# Alternative Destinations

Web service built with Flask. 

Given the IATA code of a destination along with the travel date and desired weather conditions, the service suggests three alternative destinations.

The initial version was based on *Flask Web Development*, second edition, by Miguel Grinberg (O'Reilly, 2018).

## Data Sources

Airport and destination data has been derived from [OpenFlights Airports Database](https://openflights.org/data.html) - the data is available on [GitHub](https://github.com/jpatokal/openflights/blob/master/data/airports.dat) under the [Open Database License](https://openflights.org/data.html#license).

Accurate weather data can be obtained from [World Weather Online](https://www.worldweatheronline.com), using their Local Weather API. 

This GitHub repository does not contain data as obtained from World Weather Online, but data with random modifications. The data provided here is only intended for demos of the "Alternative Destinations" web service and is not fit for any practical purpose.  

Weather data for airports can also be obtained from the [Iowa Environmental Mesonet website](https://mesonet.agron.iastate.edu/request/download.phtml?network=IN__ASOS) of Iowa State University.

Further information: data/README.txt

## Create Virtual Environment

```
virtualenv -p $(which python3.6) venv
# also works on most systems:
# python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Set Environment Variables

```
export FLASK_APP=alternative_destinations.py
export FLASK_DEBUG=1
```

## Create .env File

Example:

```
cat .env
```

```
SECRET_KEY=a_secret_key
PASSWORD_USER_01=password_for_user_01
PASSWORD_USER_02=password_for_user_02
```

## Create Dev Database

```
python create_dev_db.py 
```

## Run Tests

```
flask test
```

## Run Application

```
flask run
```

## Call

curl "http://user:password@127.0.0.1:5000/api/v1/search?iata_code=LHR&date=2019-01-31&min_temperature_celsius=5&max_temperature_celsius=20&max_precipitation_mm=0&max_cloud_cover_percent=20"

```
{"alternative_destinations":
  [
    {"iata_code": "MAD", "city": "Madrid"},
    {"iata_code": "TLV", "city": "Tel Aviv"},
    {"iata_code": "IAH", "city": "Houston"}
  ]
}
```

