#!/usr/bin/env python
import pyloopenergy
import logging
import os
from influxdb import InfluxDBClient

def elec_trace():
    json_elec = [
    {
        "measurement": "loopenergy",
        "tags": {
            "domain": "sensor",
            "type": "Electricity"
        },
        "fields": {
            "value": le.electricity_useage
        }
    }
    ]
    client.write_points(json_elec)

def gas_trace():
    json_gas = [
    {
        "measurement": "loopenergy",
        "tags": {
            "domain": "sensor",
            "type": "Gas"
        },
        "fields": {
            "value": le.gas_useage
        }
    }
    ]
    client.write_points(json_gas)

elec_serial = os.environ['elec_serial'];
elec_secret = os.environ['elec_secret'];
gas_serial = os.environ['gas_serial'];
gas_secret = os.environ['gas_secret'];
type = os.environ['type'];
influxhost = os.environ['influxhost'];
influxport = os.environ['influxport'];
influxdb = os.environ['influxdb'];

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
client = InfluxDBClient(host=influxhost, port=influxport, database=influxdb)

if type == "elec":
  le = pyloopenergy.LoopEnergy(elec_serial, elec_secret)
  le.subscribe_elecricity(elec_trace)
elif type == "elec,gas":
  le = pyloopenergy.LoopEnergy(elec_serial, elec_secret, gas_serial, gas_secret)
  le.subscribe_elecricity(elec_trace)
  le.subscribe_gas(gas_trace)
