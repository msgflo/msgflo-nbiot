#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import pytest
import json
import uuid

from msgflo_nbiot.discovery import device_discovery_msg


@pytest.fixture()
def devices_json():
    return b'''
    [
        {
            "device_name": "EVA1",
            "sensors": [
                {
                    "sensor_name": "temp",
                    "sensor_type": "int"
                }
            ]
        }
    ]
    '''


def test_discovery_json(devices_json):
    desc = json.loads(devices_json.decode('utf-8'))[0]
    msg = device_discovery_msg(desc, uuid.uuid4())

    assert msg['command'] == 'participant'
    assert msg['protocol'] == 'discovery'
    assert msg['payload']['outports'][0]['queue'] == 'EVA1/temp'
    assert msg['payload']['outports'][0]['type'] == 'int'