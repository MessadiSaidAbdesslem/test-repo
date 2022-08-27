import pickle
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("[fc94:c742:eba1:98a8:480e:98c9:a65b:3bac]",1883,60)
client.publish("dev/test",pickle.dumps("눈_눈"),0)
client.loop()

client.disconnect()
