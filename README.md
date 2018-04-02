# deerstatus
Raspberry Pi mini smart home installation

Current installation collects temperature and humidity and sends them to InfluxDB database where you can inspect them with Grafana or Chronograf.

## Hardware

* [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
* [DHT11 Sensor](https://www.adafruit.com/product/386)

## Software

* [InfluxDB](https://www.influxdata.com/time-series-platform/influxdb/) as a time series database
* [Grafana](https://grafana.com/) or 
* [Chronograf](https://www.influxdata.com/time-series-platform/chronograf/) for data visualisation 
* [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/) optionally to collect some basic metrics (CPU, RAM) from your Raspberry

