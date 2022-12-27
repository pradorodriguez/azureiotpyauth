# Welcome to this Github Repo azureiotpyauth

## In this repo you will find a Simple Python code that simulates an IoT Temperature device capable of connecting to Azure Iothub using x509 (SSL/TLS certificates) or SAS (device Connection String) authentication method. The idea is to be able to easily and quickly test multiple authentication options in your IoT application with Azure Iothub

## Along with the python code, in this repo you will find the links to deploy the Azure Components needed successfully execute the application. At this point, this is no a step by step guide, the main point is for you to understand the Python code used to develop the solution

## Guide information

### Local Environment requirements

* Internet connectivity
* [Visual Studio Code](https://code.visualstudio.com/)
* [Python version 3](https://www.python.org/downloads/)

### Azure requirements

* [An Azure subscription with administrative access](https://azure.microsoft.com/en-in/free/)
* [Azure Iothub](https://learn.microsoft.com/en-us/azure/iot-hub/iot-concepts-and-iot-hub)

### Environment set up - You might use the following links in case you want to recreate the solution

* [Create an Azure Iothub service](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-create-through-portal#create-an-iot-hub)
* Register an IoT device and choose your preferred authentication method:
  * [x509 - Follow Step 4 instructions](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-scripts#step-4---create-a-new-device)
  * [SAS - Follow the Register a new device instructions](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-create-through-portal#register-a-new-device-in-the-iot-hub)
* [If you chose x509 as your authentication method, follow this link to create required certificates](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-openssl)

### Application Code

* [The code is located in "code/app-temperature.py"]

### Python Libraries

* [azure-iot-device](https://pypi.org/project/azure-iot-device/)

### Application Notes

* If you want to test x509 authentication, make sure you follow the steps mentioned in the "If you chose x509 as your authentication method, follow this link to create required certificates" link. At the end you will need to create the following SSL/TLS objects:
  * Self Signed Certificate Authority files
    * Certificate
    * Private Key
    * Configuration File
    * Certificate Sign Request
  * Intermediate Certificate Authority files (this is OPTIONAL)
    * Certificate
    * Private Key
    * Configuration File
    * Certificate Sign Request
  * IoT Device Certificates
    * Certificate
    * Private Key
    * Certificate Sign Request

### Application main functions and methods

* Functions
  * Uncomment your preferred Authentication Method. Only one option must be uncommented
    * x509 Authentication
      * Save the device .CRT and .KEY files in the same folder as the "app-temperature.py" code
    * SaS Authentication
      * Get the connection string from the "SAS - Follow the Register a new device instructions" link.
  * Establish connectivity to Iothub
  * Create a random integer for the temperature
  * Create a dictionaru with the temperature value
  * Create a JSON object from the dictionary
  * Create a formatted message
  * Send messsage to Iothub
  * Repeat the code Infinitely

* Execute the code in a bash CLI
  * python3 app-temperature.py

## If you have any question, suggestion or comment about this repo or code, feel free to post it in this [discussion] (<https://github.com/pradorodriguez/azureiotpyauth/discussions/1>) section. I will make sure to address all your concerns
