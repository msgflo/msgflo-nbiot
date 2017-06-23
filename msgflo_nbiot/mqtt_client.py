import json
import logging
import asyncio
import datetime
from hbmqtt.client import MQTTClient, ConnectException
from hbmqtt.mqtt.constants import *
from discovery import device_discovery_msg

log = logging.getLogger(__name__)


class AsyncMQTT(object):
    def __init__(self, queue, devices):
        self.C = None
        self.queue = queue
        self.devices = devices
        self.last_discovery = datetime.datetime.now() - datetime.timedelta(seconds=11)

    async def update_mqtt(self):
        await self.C.publish('dmx-mainhall/current_state',
                             json.dumps( {'data': "bla"} ).encode('utf-8'),
                             qos=0x00, retain=True)

    async def mqtt_loop(self, loop, mqtt_server, client_id):
        url = "mqtt://{}:{}/".format(mqtt_server, 1883)
        log.debug("Connecting to MQTT server '{}'".format(url))
        self.C = MQTTClient(client_id=client_id)
        await self.C.connect(url)

        # Do the loop
        while loop.is_running():
            if (datetime.datetime.now() - self.last_discovery).seconds > 10:
                self.last_discovery = datetime.datetime.now()
                for device in self.devices:
                    msg = bytearray(json.dumps(device_discovery_msg(device, client_id)).encode('utf-8'))
                    await self.C.publish('fbp', msg, qos=0x00, retain=True)
            try:
                topic, message = self.queue.get_nowait()
                log.debug("Sending mqtt {}".format(message))
                msg_array = bytearray(message.encode('utf-8'))
                await self.C.publish(topic, msg_array, qos=0x00, retain=True)
            except asyncio.QueueEmpty:
                pass
            if self.queue.empty():
                await asyncio.sleep(0.5)
