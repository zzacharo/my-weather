import requests

from myweatherapp.location.error import NotFoundLocationError

class LocationResolver(object):
    """."""

    IPAPI_WEBAPI_URL = "https://ipapi.co/{ip_address}/json/"

    @classmethod
    def resolve(cls, ip_address):
        """."""
        res = requests.get(cls.IPAPI_WEBAPI_URL.format(ip_address=ip_address))
        if not res.ok:
            json = res.json()
            return json.get("city")
        else:
            raise NotFoundLocationError(
                msg="Location for ip {value} not found".format(
                    value=ip_address))
