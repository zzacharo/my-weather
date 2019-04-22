import json
import pytest
from flask import url_for
from datetime import date

def test_weather_api(app):
    """Test weather rest api."""
    with app.test_client() as client:
        expected_data = {
            "date": date.today().isoformat(),
            "location": "Mountain View"
        }
        res = client.get(url_for('myweatherapp_rest.index'),
                          content_type='application/json')
        assert res.status_code == 200
        response_data = json.loads(res.get_data(as_text=True))
        assert expected_data['location'] == response_data['location']
        assert expected_data['date'] == response_data['date']
        assert 'weather_status' in response_data
