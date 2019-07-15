FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
LABEL maintainer="Miguel1993"
ENV elec_serial="00000"
ENV elec_secret="00000"
ENV gas_serial="00000"
ENV gas_secret="00000"
ENV type="elec"
ENV influxhost="172.17.0.1"
ENV influxport="8086"
ENV influxdb="homeassistant"
CMD ["python","-u","run.py"]
