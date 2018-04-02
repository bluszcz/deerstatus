#!/usr/bin/env python
import time, json

import requests
import Adafruit_DHT as dht
from influxdb import InfluxDBClient

CITY = os.environ.get('DEERSTATUS_CITY', 'Barcelona')
API_KEY = os.environ.get('OPENWEATHER_APIKEY')
INFLUXDB_HOST = os.environ.get('INFLUXDB_HOST', '127.0.0.1')
sensor = dht.DHT11
pin = 4
humidity, temperature = dht.read_retry(sensor, pin)
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s' % (CITY, API_KEY)
response = requests.get(url)
data = json.loads(response.content.decode('utf-8'))
temperature_ext =  data['main']['temp']-273.5
humidity_ext =  data['main']['humidity']
wind_ext = data['wind']['speed']

time_str = time.strftime('%Y-%m-%d %H:%M:%S')

def validate(value):
    if value>-20 and value<=100:
        return True
    raise ValueError('Incorrect value %s' % value)
temperature, humidity, temperature_ext, humidity_ext = [ x if validate(x) else 0 for x in [temperature, humidity, temperature_ext, humidity_ext]]


# INFLUX DB part
db = 'iot-db'
client = InfluxDBClient(INFLUXDB_HOST, 8086, '', '', db)
host = "raspberry-01"
region = "poble-nou"
json_body = [
    {
        "measurement": "deerstatus",
        "tags": {
            "host": host,
            "region": region
        },
        "time": time_str,
        "fields": {
            "temperature_flat": float(temperature),
            "humidity_flat": float(humidity),
            "temperature_bcn": float(temperature_ext),
            "humidity_bcn": float(humidity_ext),
            "wind_bcn": float(wind_ext)
        }
    }
]
client.write_points(json_body)

