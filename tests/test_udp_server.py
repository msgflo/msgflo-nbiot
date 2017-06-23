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
                },
                {
                    "sensor_name": "hum",
                    "sensor_type": "int",
                    "sensor_id": 2,
                }
            ]
        }
    ]


def test_udp_to_mqtt(test_json):
    test_data = b'\x01\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9'
    res = list(udp_to_mqtt(test_data, test_json))
    assert res[0] == ('EVA1/temp', '160')
    assert res[1] == ('EVA1/hum', '161')

