# !/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""server.py
Usage:
  server.py <qxw_file> <positions_file> [--usb <usb_device>] [--mqtt <mqtt_server>] [--debug]

"""

import os
import sys
import json
import uuid
import asyncio
import logging
from udp_server import SensorFloProtocol
from mqtt_client import AsyncMQTT

log = logging.getLogger(__name__)


PROJECT_ROOT = os.path.join(os.path.dirname(__file__), '..')


def main():
    queue = asyncio.Queue()
    mqtt_client_id = uuid.uuid1()
    log.info('Selected {} as the current mqtt client id.'.format(mqtt_client_id))

    loop = asyncio.get_event_loop()
    udp_listen = loop.create_datagram_endpoint(SensorFloProtocol, local_addr=('0.0.0.0', 16666))
    udp_transport, udp_protocol = loop.run_until_complete(udp_listen)

    devices = json.load(open(os.path.join(PROJECT_ROOT, 'sensors.json')))
    udp_protocol.set_queue(queue)
    udp_protocol.set_devices(devices)

    mqtt_server = 'iot.eclipse.org'
    async_mqtt = AsyncMQTT(queue)
    asyncio.ensure_future(async_mqtt.mqtt_loop(loop, mqtt_server))

    try:
        log.info('Starting main loop ...')
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    log.info('Stopping main loop, closing transports ...')

    udp_transport.close()
    loop.close()


if __name__ == '__main__':
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)
    main()
