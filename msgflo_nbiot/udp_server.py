# -*- coding: utf-8 -*-
import asyncio
import logging
import struct

log = logging.getLogger(__name__)


class SensorNotFound(Exception):
    pass


def udp_to_mqtt(data, devices):
    arr = bytearray(data)
    id = arr[0]
    sensor_data = arr[1]
    for device in devices:
        for sensor in device.get('sensors', []):
            if sensor['sensor_id'] == id:
                topic = '{}/{}'.format(device['device_name'], sensor['sensor_name'])
                return (topic, '%d' % sensor_data)

    raise SensorNotFound()


class SensorFloProtocol(asyncio.DatagramProtocol):

    def __init__(self):
        self.queue = None
        self.devices = []
        super().__init__()

    def set_queue(self, queue):
        self.queue = queue

    def set_devices(self, devices):
        self.devices = devices

    def connection_made(self, transport):
        log.debug("Connection made.")
        self.transport = transport

    def datagram_received(self, data, addr):
        log.debug("Received datagram {} from host {}.".format(
            str(repr(data)),
            addr
        ))
        # TODO: Decode Data

        if self.queue != None:
            topic, message = udp_to_mqtt(data, self.devices)
            log.debug("Enqueue '{}' on topic {}.".format(message, topic))
            asyncio.ensure_future( self.queue.put((topic, message)) )
