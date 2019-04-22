import requests

from datetime import date
from myweatherapp.error import BadRequestError
from myweatherapp.weather.error import NotFoundWeatherError
from myweatherapp.models import Weather
from myweatherapp.factory import db
from myweatherapp.location.api import LocationResolver

class WeatherResolver(object):
    """."""

    WEATHER_WEBAPI_BASE_URL = "https://www.metaweather.com/api/location"

    def resolve(self, ip_location):
        """."""
        location = LocationResolver().resolve(ip_location)
        today = date.today().isoformat()
        # hash the combination of city and day to make an effective search
        # on db as hash version is used as primary key
        hash_id = hash("{}/{}".format(location, today))
        weather_today = Weather.query.filter_by(id_=hash_id).one_or_none()
        if not weather_today:
            woeid = self.search(location)
            weather_status = self.get_todays_weather(woeid)["weather_state_name"]
            weather = Weather(hash_id, weather_status, location, today)
            db.session.add(weather)
            db.session.commit()
            return weather
        else:
            return weather_today

    def search(self, location):
        """."""
        search_url = "{base}/search/?query={q}".format(
            base=self.WEATHER_WEBAPI_BASE_URL, q=location)
        res = requests.get(search_url)
        if res.ok:
            json = res.json()
            if json:
                return json[0]["woeid"]
            else:
                raise NotFoundWeatherError(
                    msg="Weather for location {} not found".format(location))
        else:
            raise BadRequestError(
                msg="Something went wrong!")

    def get_todays_weather(self, woeid):
        """."""
        WEATHER_WEBAPI_DEATAILS_URL = "{base}/{id}/".format(
            base=self.WEATHER_WEBAPI_BASE_URL,
            id=woeid)
        res = requests.get(WEATHER_WEBAPI_DEATAILS_URL)
        if res.ok:
            json = res.json()
            if json.get("details") == "Not found.":
                raise NotFoundWeatherError(
                    msg="Weather for location {} not found".format(location))
            else:
                # return only the first result as we need only the today's
                # weather
                return json["consolidated_weather"][0]
            return res["weather_state_name"]
        else:
            raise BadRequestError(
                msg="Something went wrong!")