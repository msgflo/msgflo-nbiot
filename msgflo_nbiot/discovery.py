def device_discovery_msg(device_desc, client_id):
    """
    Send the discovery message, such that MsgFlo can automatically set up a component
    whenever a new instance of this program is run.
    Details, see: https://github.com/c-base/mqttwebview/issues/2
    """
    device_name = device_desc['device_name']
    outports = []
    for sensor in device_desc['sensors']:
        sensor_name = sensor.get('sensor_name')
        sensor_type = sensor.get('sensor_type')

        port = {
            "queue": "{}/{}".format(device_name, sensor_name),
            "type": "{}".format(sensor_type),
            "description": "Sensor value",
            "id": "{}".format(sensor_name),
        }
        outports.append(port)
    discovery_message = {
        "command": "participant",
        "protocol": "discovery",
        "payload": {
            "component": "c-base/eva",
            "label": "{}".format(device_name),
            "inports": [],
            "outports": outports,
            "role": "{}".format(device_name),
            "id": '{}'.format(client_id),
            "icon": "rocket"
        },
    }
    return discovery_message
    #log.debug("Sending FBP discovery message.")
    #client.publish('fbp', payload=json.dumps(discovery_message).encode('utf-8'), qos=0)