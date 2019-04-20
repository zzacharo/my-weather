import requests

from myweatherapp.location.error import NotFoundLocationError
from myweatherapp.error import BadRequestError

class LocationResolver(object):
    """."""

    IPAPI_WEBAPI_URL = "https://ipapi.co/{ip_address}/json/"

    def resolve(self, ip_address):
        """."""
        res = requests.get(self.IPAPI_WEBAPI_URL.format(ip_address=ip_address))
        if res.ok:
            json = res.json()
            if "city" in json:
                return json["city"]
            else:
                raise NotFoundLocationError(
                    msg="Location for ip {value} not found".format(
                        value=ip_address))
        else:
            raise BadRequestError(
                msg="Something went wrong!")