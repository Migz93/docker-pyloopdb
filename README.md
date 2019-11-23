# pyloopdb
[![Docker Version](https://images.microbadger.com/badges/version/miguel1993/docker-pyloopdb.svg)](https://microbadger.com/images/miguel1993/docker-pyloopdb) [![Docker Image](https://images.microbadger.com/badges/image/miguel1993/docker-pyloopdb.svg)](https://microbadger.com/images/miguel1993/docker-pyloopdb) [![Docker Pulls](https://img.shields.io/docker/pulls/miguel1993/docker-pyloopdb.svg)](https://microbadger.com/images/miguel1993/docker-pyloopdb) [![Docker Stars](https://img.shields.io/docker/stars/miguel1993/docker-pyloopdb.svg)](https://microbadger.com/images/miguel1993/docker-pyloopdb) [![License MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Pull data from loopenergy using pyloopenergy module and then write this to influxdb.

Thanks to [pavoni](https://github.com/pavoni) for his work on creating [pyloopenergy](https://github.com/pavoni/pyloopenergy), without it this script/container wouldn't have been possible.

This connects to [Loop Energy](https://www.your-loop.com/), takes the data received from loop energy for electricity/gas usage and writes it to an influx database. (Influxdb needs to be installed/configured seperately.)

This was created for myself as currently the homeassistant loop energy component is not working and my python experience is nowhere near the level required to work out what's wrong with the component. As others may find this handy I thought I would share it.
<br>I only really use homeassistant to amalgamate all my home IOT devices and then pass the data through to influx to be displayed in Grafana so this just cuts out the middleman.

Usage
------

<b>Docker create command for only electricity monitoring.</b>
```Docker
docker create \
  --name=pyloopdb \
  -e elec_serial=00000 \
  -e elec_secret=00000 \
  -e type=elec \
  -e influxhost=172.17.0.1 \
  -e influxport=8086 \
  -e influxdb=homeassistant \
  --restart unless-stopped \
  miguel1993/pyloopdb
```

<b>Docker create command for electricity and gas monitoring. (Untested as I don't have gas monitoring)</b>
```Docker
docker create \
  --name=pyloopdb \
  -e elec_serial=00000 \
  -e elec_secret=00000 \
  -e gas_serial=00000 \
  -e gas_secret=00000 \
  -e type=elec,gas \
  -e influxhost=172.17.0.1 \
  -e influxport=8086 \
  -e influxdb=homeassistant \
  --restart unless-stopped \
  miguel1993/pyloopdb
```

Parameters
------
```
elec_serial                  Configured with your elec serial from loop.
elec_secret                  Configured with your elec secret from loop.
gas_serial                   Configured with your gas serial from loop. Optional.
gas_secret                   Configured with your gas secret from loop. Optional.
type                         Type of monitoring you want, choices are `elec` & `elec,gas`.
influxhost                   URL/IP that the influx database can be accessed on.
influxport                   Port that the influx database is running on.
influxdb                     The database in influx that you want to write to.
```

Versions
------
* 16.07.2019: - Modified to write to the "W" series in influxdb & to also send data in Watts.
* 15.07.2019: - Initial release.

Note
------
* The measurement is written to the influx database in Watts as all my other IOT devices report in Watts.
* It should be possible to run the python script directly, rather then running it in a container. You'd just need to set the variables rather than have them load.
* I only have a very basic understanding of python, just about enough to get things to work, so if you see anything that could be improved please let me know.
