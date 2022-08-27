import paho.mqtt.client as paho
import pickle
import cv2

img = cv2.imread('./kekyou.png')

client = paho.Client()

if client.connect("[fc94:c742:eba1:98a8:480e:98c9:a65b:3bac]", 1883 , 60) != 0 :
    print("Could not connect to MQTT broker!")

#while True:
client.publish("dev/test", pickle.dumps(img), 1)

client.loop()

client.disconnect()

#os.system('mosquitto_pub -h cheima -t "dev/test" -m "test"')