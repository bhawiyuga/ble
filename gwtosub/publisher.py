import threading

import paho.mqtt.client as mqtt
import threading
import time

ip = "45.76.186.85"
port = 1884
topic = "/node"
message = "Hello"
# Jumlah concurrent client atau device
num_client = 1
# Jumlah pengiriman message
num_iter = 10
# Jeda waktu pengiriman (dalam detik)
sim_delay = 500

class PubThread(threading.Thread):
    def run(self):
        mqttc = mqtt.Client(transport="websockets")
        mqttc.connect(ip, port)
        for i in range(0, num_iter) :
            time_str = str(time.time())
            mqttc.publish(topic, time_str)
            time.sleep(sim_delay/1000)


for i in range(0,num_client):
    t1 = PubThread()
    t1.start()
