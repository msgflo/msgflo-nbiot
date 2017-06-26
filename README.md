# msgflo-nbiot [![Build Status](https://travis-ci.org/msgflo/msgflo-nbiot.svg?branch=master)](https://travis-ci.org/msgflo/msgflo-nbiot)
Narrowband IoT gateway for MsgFlo, this is the server-side part of a project built for the Deutsche Telekom NB-IOT Hackathon, Berlin, Germany, 2017. 

The client-side part is documented here: https://ansi.23-5.eu/2017/06/nb-iot-bc95-arduino/

## How to run the tests

- create a virtualenv
- pip install -r requirements.txt
- pytest

## Docker docker, container, container

### To build and push
- docker build . -t msgflo/msgflo-nbiot
- docker login
- docker push msgflo/msgflo-nbiot

# To run
- docker run -d -p 16666:16666/udp msgflo/msgflo-nbiot
