import requests

from myweatherapp.error import BadRequestError
from myweatherapp.weather.error import NotFoundWeatherError

class WeatherResolver(object):
    """."""

    WEATHER_WEBAPI_BASE_URL = "https://www.metaweather.com/api/location"

    def resolve(self, location):
        """."""
        woeid = self.search(location)
        return self.get_today_weather(woeid)["weather_state_name"]

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

    def get_today_weather(self, woeid):
        """."""
        details_url = "{base}/{id}/".format(
            base=self.WEATHER_WEBAPI_BASE_URL,
            id=woeid)
        res = requests.get(details_url)
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