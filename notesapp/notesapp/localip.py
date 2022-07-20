import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

LOCAL_IP_ADDRESS = s.getsockname()[0]