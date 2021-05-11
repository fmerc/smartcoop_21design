# 2021 Design Challenge: Smartcoop (prototype) #

An IoT gadget for chicken coops, provides temperature & humidity monitoring, and a live-feed security camera. This project was developed on a Raspberry Pi Zero W. We used the [Blynk](https://blynk.io/) platform to remotely interface with the system.

## Features ##
- Monitor temperature and humidity remotely.
- Temp & Humidity Monitoring: The temperature and humidity readings are displayed with Blynk.
- Temp & Humidity Control: If the system is connected to a heat source, the user can set a temperature from an app for the system to maintain like a thermostat. If the system is connected to a ventilation or fan, it can manually be turned on or off from the app. We represented heater and fan with LEDs to test and demonstrate the control.
- Live Camera Feed: The device streams live video from the onboard camera over WiFi. For now, it is viewable at an http address in any browser on the same network. Currently it is not viewable on Blynk for iOS, and often freezes on Blynk for Android. 


## Hardware Used ##
Board: Raspberry Pi Zero W. Expected to work on other Pi models, but not tested.\
Sensor: AM2320 DTH. Store page and documentation found here: https://www.adafruit.com/product/3721 \
Camera: OV5467. We used a cheap one from [Amazon](https://www.amazon.com/Makerfocus-Raspberry-Camera-Vision-Infrared/dp/B073HYJDCM/ref=pd_lpo_147_t_1/141-3134479-3297410?_encoding=UTF8&pd_rd_i=B073HYJDCM&pd_rd_r=87e6c35e-dd3f-4452-a644-da6c61f125a1&pd_rd_w=FpmXb&pd_rd_wg=SbBAy&pf_rd_p=337be819-13af-4fb9-8b3e-a5291c097ebb&pf_rd_r=REF3QBQXA7D6M44J2ZSX&refRID=REF3QBQXA7D6M44J2ZSX&th=1), but any Pi-compatible camera is expected to work.\
LEDs: 3-5V, 5-10mA. Any LED that meets the GPIO specs of your board should work



## WIP (no order) ##
- Learn how to make our own app to integrate with the system better.
  - None of us are programmers
- Add option to switch between automatic control "thermostat" and manual mode
- Stream video to Blynk app
  - Optimize video streaming script for better performance
  - Integrate video stream directly with Blynk instead of open http address
- Replace LEDs with 5V relay switches to control heater/fan with


## Connections & Schematic ##
