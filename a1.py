# NAME: Adwit Singh Kochar
# ROLL NO.: 2018276
# SECTION: B
# GROUP: 5

# --------------------------------------
# Function to get weather response
# --------------------------------------
def weather_response(location, API_key):
	"""Returns a JSON string that is a response to a weather query"""

	import urllib.request
	url = 'http://api.openweathermap.org/data/2.5/forecast?q='+location+'&APPID='+API_key
	page = urllib.request.urlopen(url)
	return str(page.read())
	 
# --------------------------------------
# Function to check for valid response 
# --------------------------------------
def has_error(location,json):
	"""Returns True if the input location and response city name is not matched"""
	
	a = json.find('name')							# Finding name of city in JSON
	start = a + 7
	end = json.find('"', start)
	city = json[start:end]
	
	if location.lower() != city.lower():
		return True
	
	return False

# --------------------------------------
# Function to get attributes on nth day
# --------------------------------------

#***************************************
# 1. Temperature
#***************************************
def get_temperature (json, n=0, t='3:00:00'):
	"""Returns temperature of nth day from current day at t time"""
	
	import datetime 													# Converting date-time to standard format
	date_diff = datetime.timedelta(days=n)
	date = str(datetime.date.today() + date_diff)
	reqdatetime = str(datetime.datetime.strptime( date + t , "%Y-%m-%d%H:%M:%S"))

	a = json.find(reqdatetime)											# Searching the required date and time
	
	if a == -1 :														# Date-Time not found
		print('ERROR: Date/Time not available')
		return

	pos = json.rfind('"temp":', 0 , a )									# Extracting temperature
	start = pos + 7
	end = json.find(',', start)
	temp = json[start:end]
	return float(temp)

#***************************************
# 2. Humidity
#***************************************
def get_humidity(json, n=0, t='3:00:00'):
	"""Returns humidity of nth day from current day at t time"""

	import datetime 													# Converting date-time to standard format
	date_diff = datetime.timedelta(days=n)
	date = str(datetime.date.today() + date_diff)
	reqdatetime = str(datetime.datetime.strptime( date + t , "%Y-%m-%d%H:%M:%S"))

	a = json.find(reqdatetime)											# Searching the required date and time
	
	if a == -1 :														# Date-Time not found
		print('ERROR: Date/Time not available')
		return

	pos = json.rfind('"humidity":', 0 , a )								# Extracting humidity
	start = pos + 11
	end = json.find(',', start)
	humidity = json[start:end]
	return int(humidity) 

#***************************************
# 3. Pressure
#***************************************
def get_pressure(json, n=0, t='3:00:00'):
	"""Returns pressure of nth day from current day at t time"""

	import datetime 													# Converting date-time to standard format
	date_diff = datetime.timedelta(days=n)
	date = str(datetime.date.today() + date_diff)
	reqdatetime = str(datetime.datetime.strptime( date + t , "%Y-%m-%d%H:%M:%S"))

	a = json.find(reqdatetime)											# Searching the required date and time
	
	if a == -1 :														# Date-Time not found
		print('ERROR: Date/Time not available')
		return

	pos = json.rfind('"pressure":', 0 , a )								# Extracting pressure
	start = pos + 11
	end = json.find(',', start)
	pressure = json[start:end]
	return float(pressure) 

#***************************************
# 4. Wind
#***************************************
def get_wind(json, n=0, t='3:00:00'):
	"""Returns wind speed of nth day from current day at t time"""

	import datetime 													# Converting date-time to standard format
	date_diff = datetime.timedelta(days=n)
	date = str(datetime.date.today() + date_diff)
	reqdatetime = str(datetime.datetime.strptime( date + t , "%Y-%m-%d%H:%M:%S"))

	a = json.find(reqdatetime)											# Searching the required date and time
	
	if a == -1 :														# Date-Time not found
		print('ERROR: Date/Time not available')
		return

	pos = json.rfind('"speed":', 0 , a )								# Extracting wind speed
	start = pos + 8
	end = json.find(',', start)
	wind = json[start:end]
	return float(wind) 

#***************************************
# 5. Sea Level
#***************************************
def get_sealevel(json, n=0, t='3:00:00'):
	"""Returns sea level of nth day from current day at t time"""

	import datetime 													# Converting date-time to standard format
	date_diff = datetime.timedelta(days=n)
	date = str(datetime.date.today() + date_diff)
	reqdatetime = str(datetime.datetime.strptime( date + t , "%Y-%m-%d%H:%M:%S"))

	a = json.find(reqdatetime)											# Searching the required date and time
	
	if a == -1 :														# Date-Time not found
		print('ERROR: Date/Time not available')
		return

	pos = json.rfind('"sea_level":', 0 , a )							# Extracting sea level
	start = pos + 12
	end = json.find(',', start)
	sealevel = json[start:end]
	return float(sealevel) 




