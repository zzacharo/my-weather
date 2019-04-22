class NotFoundWeatherError(Exception):

    def __init__(self, msg):
        """."""
        self.msg = msg
        self.code = 404
