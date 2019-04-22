# myweatherapp

My weather app example application for code review test.

## Getting started

To better isolate the packages required by this project from the system
ones we will create a virtual environment:

```console
$ mkvirtualenv myweatherapp -p python3.6
(myweatherapp) $ pip install .
```

We can now initialize the database:

```console
$ ./scripts/setup
```

Run the application on your computer:

```console
  (myweatherapp) $ export FLASK_APP=myweatherapp/app.py
  (myweatherapp) $ flask run
```

Get the weather of your location for the current day using the REST API:

```console
$ curl -X GET http://0.0.0.0:5000/api/weather \
  -H "Content-Type: application/json"  \
{
  "date": "2019-04-22",
  "location": "Mountain View",
  "weather_status": "Light Cloud"
}
```

**NOTE**:
Clearly, running your app locally with a local IP address, `localhost` or `127.0.0.1`, will not help to resolve it to a real location. When you are developing, simply hardcode a test IP of your preference in the `config.py` file.

```python
TEST_IP = "8.8.8.8"
```

## Development

In order to have a better developer experience you can install the package
in editable mode and you can run the `scripts/server` script. This will run flask with the debug flag, so the application
gets refreshed with your code changes:

```console
  (myweatherapp) $ pip instal -e .
  (myweatherapp) $ ./scripts/server
```

## Tests

To run tests:

```console
$ python setup.py test
```

## Managing the database

To create the database:

```console
$ flask run weather db init
Database successfully initialized.
```

To empty the database:

```console
$ flask run weather db init
Database successfully dropped.
```
