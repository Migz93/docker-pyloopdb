#!/usr/bin/env python
import pyloopenergy
import logging
import os
from influxdb import InfluxDBClient


def elec_trace():
    elec_usaeage = le.electricity_usage * 1000
    json_elec = [
      {
        "measurement": "W",
        "tags": {
            "domain": "sensor",
            "entity_id": "loopenergy_elec",
            "friendly_name": "loopenergy_elec"
        },
        "fields": {
            "value": elec_usaeage
        }
      }
    ]
    client.write_points(json_elec)


def gas_trace():
    json_gas = [
      {
        "measurement": "W",
        "tags": {
            "domain": "sensor",
            "entity_id": "loopenergy_gas",
            "friendly_name": "loopenergy_gas"
        },
        "fields": {
            "value": le.gas_useage
        }
      }
    ]
    client.write_points(json_gas)

elec_serial = os.environ['elec_serial']
elec_secret = os.environ['elec_secret']
gas_serial = os.environ['gas_serial']
gas_secret = os.environ['gas_secret']
type = os.environ['type']
influxhost = os.environ['influxhost']
influxport = os.environ['influxport']
influxdb = os.environ['influxdb']

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
client = InfluxDBClient(host=influxhost, port=influxport, database=influxdb)

if type == "elec":
    le = pyloopenergy.LoopEnergy(elec_serial, elec_secret)
    le.subscribe_elecricity(elec_trace)
elif type == "elec,gas":
    le = pyloopenergy.LoopEnergy(elec_serial, elec_secret,
                                 gas_serial, gas_secret)
    le.subscribe_elecricity(elec_trace)
    le.subscribe_gas(gas_trace)
