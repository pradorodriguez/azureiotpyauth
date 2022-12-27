import time
import uuid
from random import randint
# JSON library
import json
# Azure IoT SDK for Python - pip3 install azure-iot-device
from azure.iot.device import X509
from azure.iot.device import IoTHubDeviceClient
from azure.iot.device import Message


###  IOTHUB AUTHENTICATION - Uncomment the authentication method you want to use
## x509 Authentication
## Create x509 Iot device class instance with the location of the SSL certificate and private key
    ## https://learn.microsoft.com/en-us/python/api/azure-iot-device/azure.iot.device.x509?view=azure-python
# x509 = X509(
#     cert_file="<device-certificate-filename>.crt",
#     key_file="<device-private-key-filename>.key"
# )
## Create IoT device client instance using x509 CA authentication
    ## https://learn.microsoft.com/en-us/python/api/azure-iot-device/azure.iot.device.aio.iothubdeviceclient?view=azure-python#azure-iot-device-aio-iothubdeviceclient-create-from-x509-certificate
# device_client = IoTHubDeviceClient.create_from_x509_certificate(
#     x509=x509,
#     hostname="<iothub-hostname-fqdn>",
#     device_id="<device-id-in-iothub>"
# )
## SAS Authentication
## Create IoT device client instance using SAS authentication (device connection string)
    ## https://learn.microsoft.com/en-us/python/api/azure-iot-device/azure.iot.device.aio.iothubdeviceclient?view=azure-python#azure-iot-device-aio-iothubdeviceclient-create-from-connection-string
# connection_string = "<device-connection-string-in-iothub>"
# device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)
# device_client.connect()

# Connect to IoT Hub
device_client.connect()

# Infinite loop to send messages to IoT Hub
while True:
    # Create the telemetry data using random values and save it to a Dictionary
    temperature = randint(15, 40)
    print(f' Temperature: {temperature}°C')
    temp_dict = {"temperature": temperature}
    # Convert the Dictionary to JSON
    json_temp = json.dumps(temp_dict)
    # Create a message using the JSON data to send it to IoT Hub
    msg = Message(json_temp)
    msg.message_id = uuid.uuid4()
    msg.content_encoding = "utf-8"
    msg.content_type = "application/json"
    # Send the message to IoT Hub
    device_client.send_message(msg)

    # Wait 3 seconds before sending the next message
    time.sleep(3)