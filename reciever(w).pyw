from vidstream import StreamingServer
import threading

reciever = StreamingServer("192.168.31.108", 9999)

t = threading.Thread(target=reciever.start_server)
t.start()

while input("") != "STOP":
    continue
    
reciever.stop_server()