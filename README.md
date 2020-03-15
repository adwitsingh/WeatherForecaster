# WeatherForecaster
Python application which gets weather data using OpenWeatherMap API and extracts information like temperature, humidity etc. using string manipulation

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This project needs python3 installed on the local machine along with *datetime* and *urllib*, which can be installed using:

```bash
python3 -m pip install datetime
python3 -m pip install urllib
```



### Installing

a1.py contains all the functions for getting data using API and extracting temperature, humidity etc.

1. ***weather_response(location, API_key)*** : returns JSON string that is response to the weather query for given location.

```python
from a1 import weather_response
```

2. ***has_error(location,json)*** : returns TRUE if input location and response city name don't match.

```python
from a1 import has_error
```

3. ***has_"X" (json, n, t)*** : return X attribute of n<sup>th</sup> day from current day at **t** time.

   *Here X = {temperature, humidity, pressure, wind, sealevel}*

```python
from a1 import get_X
```



## Running the tests

Some test have been included which can be run using:
```
python3 a1test.py
```

NOTE: the JSON strings in a1test.py need to be updated before running the tests.

## Authors

* **Adwit Singh Kochar** - *Initial work* - [adwitsingh](https://github.com/adwitsingh)
