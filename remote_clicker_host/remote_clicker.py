import socket
from pyautogui import keyDown, keyUp
import time
from threading import Thread

PORT = 4000
#IP = socket.gethostbyname(socket.gethostname())
IP = "192.168.137.1"
BUFF_SIZE = 32

KEYS = "abcdefghijklmnopqrstuvwxyz1234567890"
DELAY = 0.10
# List of tuples with the keys being pressed and the ms remained 
pressed = {}

def pressKey(key):
    keyDown(key)
    time.sleep(DELAY)
    keyUp(key)

# Create the UDP Server and host it
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = (IP, PORT)
s.bind(server_address)
print("Listening on", server_address)

def listenForUDP():
    while True:
        #print("...")
        data, address = s.recvfrom(BUFF_SIZE)
        key = data.decode('utf-8')[0]
        #print("> Received from", address, ":", key)
        
        #print("pressed", key)
        Thread(target=pressKey, args=(key, )).start()
        

# This thread will listen for incoming messages and add the keys to the list
listenThread = Thread(target=listenForUDP)

# Start listening and responding to key request
listenThread.start()