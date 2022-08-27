import paho.mqtt.client as mqtt
import pickle

def on_message(client, userdata, message):
    print(message.topic+ ": " + str(pickle.loads(message.payload)))

client = mqtt.Client()
client.connect("[fc94:c742:eba1:98a8:480e:98c9:a65b:3bac]",1883,60)
client.subscribe("dev/test",0)
client.on_message = on_message

try:
    client.loop_forever()
except:
    print("disconnected from broker...")
    
client.disconnect()