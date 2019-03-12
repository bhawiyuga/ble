import threading

import paho.mqtt.client as mqtt
import threading
import time

ip = "45.76.186.85"
port = 1884
topic = "/node"
message = "Hello"
# Jumlah concurrent device
num_device = 1
# Jumlah pengiriman message
num_iter = 10
# Jeda waktu pengiriman (dalam detik)
sim_delay = 1

class PubThread(threading.Thread):
    def run(self):
        for i in range(0, num_iter) :
            send_time = time.time()
            send_time_str = str(send_time)
            # To do : Kirim message berisi send_time ke BLE

            # To do : Baca response berisi send time
            recv_time = time.time()
            # To do : delay = recv_time - send_time
            delay = recv_time - send_time
            # To do : cetak delay ke layar
            print(delay)
            # Jeda pengiriman
            time.sleep(sim_delay)


for i in range(0,num_device):
    t1 = PubThread()
    t1.start()
