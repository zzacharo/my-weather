# Code Review Test

This is a boilerplate of a Flask App with only one simple homepage displaying "Nice weather at CERN!".

The goal of this exercise would be to extend/modify this code and implement a few tasks. The tasks should not take you very long (~2 or 3 hours in total), and the idea is to have some code that we can review together the day of the interview.

## App

We would like to create a very simple application that, given an HTTP request, it shows the weather of the city of the user, for **today only**. To keep it simple (even if not reliable) we would like to use the IP address location of the request.

For example, when opening the homepage of your app, the expected outcome should be something like:

```
Today, the weather in Geneva is Clear.
```

We foreseen that this application will have quite of a success! We expect to start with about 10 requests per minute.
Moreover, we would like to store and record the weather of each day for each city requested, in case we will want to make it available in the future to our users.

To summarize, the app should:

1. display the weather of the user's city for today, based on the IP of the request
2. store the data for each day for the requested cities (based only on user requests, no `async` jobs)
3. be able to serve all our users with an acceptable response time, while depending on external services to retrieve location and weather data
4. [optional] if you have some time, it would be nice that the frontend communicates with the backend through a REST API call.

### Web services

We can take advantage of a couple of nice web services available on the internet for free.

### IP Location APIs

[ipapi](https://ipapi.co/#api) can retrieve the location of a given IP address. For example:

```
$ curl https://ipapi.co/8.8.8.8/json/
{
    "ip": "8.8.8.8",
    "city": "Mountain View",
    "region": "California",
    "region_code": "CA",
    "country": "US",
    "country_name": "United States",
    "continent_code": "NA",
    "in_eu": false,
    "postal": "94035",
    "latitude": 37.386,
    "longitude": -122.0838,
    "timezone": "America/Los_Angeles",
    "utc_offset": "-0700",
    "country_calling_code": "+1",
    "currency": "USD",
    "languages": "en-US,es-US,haw,fr",
    "asn": "AS15169",
    "org": "Google LLC"
}
```

### Weather APIs

[MetaWeather](https://www.metaweather.com/api/) is a free API service that returns the weather forecast for the next 5 days of a given location.

First, retrieve the location ID:

```bash
$ curl "https://www.metaweather.com/api/location/search/?query=Mountain+View"
[
  {
    "title": "Mountain View",
    "location_type": "City",
    "woeid": 2455920,
    "latt_long": "37.39999,-122.079552"
  }
]
```

Then, retrieve the forecast for the `woeid` `2455920`:

```bash
$ curl "https://www.metaweather.com/api/location/2455920/"
{
  "consolidated_weather": [
    {
      "id": 6267468718800896,
      "weather_state_name": "Heavy Rain",
      "weather_state_abbr": "hr",
      "wind_direction_compass": "WSW",
      "created": "2019-04-15T19:56:41.618036Z",
      "applicable_date": "2019-04-15",
      "min_temp": 8.280000000000001,
      "max_temp": 17.155,
      "the_temp": 17.37,
      "wind_speed": 2.8057380895569874,
      "wind_direction": 254.5,
      "air_pressure": 1011.89,
      "humidity": 65,
      "visibility": 9.040950847053209,
      "predictability": 77
    },
    ...
}
```

### If something is wrong

You are free to use any other web service:

* IP Location: https://github.com/toddmotto/public-apis/blob/master/README.md#geocoding
* Weather APIs: https://github.com/toddmotto/public-apis/blob/master/README.md#weather

If nothing really works for you, don't worry: please pretend that there is a web service available and complete the exercise with a fake API response.

## Run

```
  $ cd myweather
  $ pip install -r requirements.txt
  $ export FLASK_APP=myweatherapp/app.py FLASK_ENV=development
  $ flask run
```

## How to test

Clearly, running your app locally with a local IP address, `localhost` or `127.0.0.1`, will not help to resolve it to a real location. When you are developing, simply hardcode a test IP of your preference in the `config.py` file.

```python
TEST_IP = "8.8.8.8"
```

When opening the homepage the first time, you should see:

`Current IP address: 8.8.8.8`
