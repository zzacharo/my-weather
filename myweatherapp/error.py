class BadRequestError(Exception):

    def __init__(self, msg):
        """."""
        self.msg = msg
        self.code = 500
