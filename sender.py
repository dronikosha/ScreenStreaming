from vidstream import ScreenShareClient
import threading


IP = ""
sender = ScreenShareClient(IP, 9999)
sender.start_stream()

t = threading.Thread(target=sender.start_stream())
t.start()

while input("") != "STOP":
    continue
    
sender.stop_stream()

# Для запуска без консоли надо start pythonw название_файла