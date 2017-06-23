#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import pytest
import json
import uuid

from msgflo_nbiot.udp_server import udp_to_mqtt


@pytest.fixture
def test_json():
    return [
        {
            "device_name": "EVA1",
            "sensors": [
                {
                    "sensor_name": "temp",
                    "sensor_type": "int",
                    "sensor_id": 1,
                }
            ]
        }
    ]


def test_udp_to_mqtt(test_json):
    test_data = b'\x01\x01\x00\x00\x00'
    assert udp_to_mqtt(test_data, test_json) == ('EVA1/temp', 1)
