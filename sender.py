from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient("192.168.31.108", 9999)
sender.start_stream()

t = threading.Thread(target=sender.start_stream())
t.start()

while input("") != "STOP":
    continue
    
sender.stop_stream()