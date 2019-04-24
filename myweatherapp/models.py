"""
Write your models in this file.

You can use the imported `db` like:

class MyModel(db.Model):
    pass
"""

from myweatherapp.factory import db

class Weather(db.Model):
    """Represents the weather for a specific day and city."""
    id_ = db.Column(db.Integer, primary_key=True, autoincrement=False)
    status = db.Column(db.String(80))
    location = db.Column(db.String(80))
    day = db.Column(db.String(80))

    def __init__(self, id, status, location, day):
        """Initialize Weather model."""
        self.id_ = id
        self.status = status
        self.location = location
        self.day = day

    def dumps(self):
        return {
            "weather_status": self.status,
            "location": self.location,
            "date": self.day
        }