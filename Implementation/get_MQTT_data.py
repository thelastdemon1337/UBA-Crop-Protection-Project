         

import paho.mqtt.client as mqtt
import os
import random
from pydub import AudioSegment
from pydub.playback import play
import RPi.GPIO as GPIO
import time

# LED FUNCTIONALITY

LED_PIN = 17

MQTT_ADDRESS = '192.168.2.103'
MQTT_USER = 'testUser'
MQTT_PASSWORD = 'test'
MQTT_TOPIC = 'boar/alert'

def on_connect(client, userdata, flags, rc):
    """ The callback for when the client receives a CONNACK response from the server."""
    print('Connected with result code ' + str(rc))
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    """The callback for when a PUBLISH message is received from the server."""
    print(msg.topic + ' ' + str(msg.payload))
    if str(msg.payload):
        path = '/home/pi/Desktop/audio'
        audios = os.listdir(path)
        d = random.choice(audios)
        play(AudioSegment.from_mp3(path + '/' + d))
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(LED_PIN, GPIO.OUT)
        i = 0
        while(i < 10):
            GPIO.output(LED_PIN,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_PIN,GPIO.LOW)
            time.sleep(0.5)
            i += 1

        GPIO.cleanup()

def main():
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect(MQTT_ADDRESS, 1883)
    mqtt_client.loop_forever()


if __name__ == '__main__':
    print('MQTT to InfluxDB bridge')
    main()