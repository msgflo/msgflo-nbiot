#!/usr/bin/env python3
import socket

UDP_IP = "ansi.23-5.eu"
UDP_PORT = 16666
MESSAGE = b'\x01\xff'

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
