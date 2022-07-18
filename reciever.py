from vidstream import StreamingServer
import threading

reciever = StreamingServer(IP, 9999)

t = threading.Thread(target=reciever.start_server)
t.start()

while input("") != "STOP":
    continue
    
reciever.stop_server()