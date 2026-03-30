import threading
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883

topic = "mq-chat/spse/d32"

def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected with result code {rc}")

def on_message(client, userdata, msg):
    print(f"Recieved message: {msg.payload.decode()} on topic {msg.topic}")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, keepalive=60)

client.subscribe(topic)
def user_input():
    while True:
        text=input()
        client.publish(topic, "[s]"+text)

threading.Thread(target=user_input,daemon=True).start()

client.loop_forever()