import requests

from flask import current_app
from myweatherapp.location.error import NotFoundLocationError
from myweatherapp.error import BadRequestError

class LocationResolver(object):
    """."""

    IPAPI_WEBAPI_URL = "https://ipapi.co/{ip_address}/json/"

    def resolve(self, ip_address):
        """."""
        cache = current_app.config['cache']
        try:
            location = cache.get(ip_address).decode()
            return location
        except KeyError as e:
            res = requests.get(self.IPAPI_WEBAPI_URL.format(ip_address=ip_address))
            if res.ok:
                json = res.json()
                if "city" in json:
                    cache.put(ip_address, json["city"].encode())
                    return json["city"]
                else:
                    raise NotFoundLocationError(
                        msg="Location for ip {value} not found".format(
                            value=ip_address))
            else:
                raise BadRequestError(
                    msg="Something went wrong!")