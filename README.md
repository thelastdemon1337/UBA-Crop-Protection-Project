# UBA-Crop-Protection-Project

### Wild boars are one of the major problems for farmers whose land is nearby to the forest. To stop the wild boars entering into the farm, we developed an IoT device that can detect the wild Boars and give loud alert sounds to scare the wild Boars along with iridium lights glowing partially. The main theme of this project is to save the crop from wild animals without harming them.

###Considering this as a problem statement of saving the crop as well as the wide boar we came up with a solution using the technology of the internet of things. This project will be using a PIR sensor, node MCU module, Raspberry Pi and a speaker.
My solution goes in such a way that whenever a wild Boar is detected by PIR sensor the information is forwarded to the Raspberry Pi 3 which receives the message from the PIR sensor and accordingly place multiple soundtracks using a loudspeaker like gun firing, dog shouting, people shouting and other scary sounds along with multiple iridium lights glowing randomly. 

###Here, the PR sensors are placed along with the parameter of the field covering the Rangers according to each PIR sensor. The PIR sensor is connected to the node MCU board, which has an inbuilt Wi-Fi module. Whenever the PIR sensor detects some motion before them, it sends an alert message to the Raspberry Pi using the MQTT server.


## I learned dealing with Arduino , Raspberry pi, linux cron jobs, creating unix Systemctl services , mqtt for data sharing, etc through this project.
