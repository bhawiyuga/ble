import paho.mqtt.client as mqtt
import threading
import time

ip = "45.76.186.85"
port = 1884
topic = "/node"
message = "Hello"

num_client = 1
num_iter = 1

list_thread = []

class SubThread(threading.Thread):
    is_running = True
    mqttc = None

    def stopThread(self):
        self.mqttc.loop_stop()

    def on_message(self, mosq, obj, msg):
        #print(msg.payload)
        time_start = float(msg.payload)
        #print(time_start)
        time_end = time.time()
        delay = time_end - time_start
        print(delay)

    def run(self):
        #print("tes")
        self.mqttc = mqtt.Client(transport="websockets")
        self.mqttc.connect(ip, port)
        self.mqttc.subscribe(topic)
        self.mqttc.on_message = self.on_message
        self.mqttc.loop_start()


for i in range(0,num_client):
    t1 = SubThread()
    list_thread.append(t1)
    t1.start()

try :
    while True:
        pass
except KeyboardInterrupt:
    for i in list_thread :
        i.stopThread()
    print("The end")
