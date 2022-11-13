import socket
from pyautogui import press, keyDown, keyUp
import time
import threading

PORT = 4000
IP = socket.gethostbyname(socket.gethostname())

KEYS = "abcdefghijklmnopqrstuvwxyz1234567890"
DELAY = 0.10
# List of keys to be pressed
toBePressed = []
# List of tuples with the keys being pressed and the ms remained 
pressed = []

# Create the UDP Server and host it
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = (IP, PORT)
s.bind(server_address)
print("Listening on", server_address)

def listenForUDP():
    while True:
        print("...")
        data, address = s.recvfrom(4096)
        key = data.decode('utf-8')[0]
        print("> Received from", address, ":", key)
        
        if key in KEYS:
            toBePressed.append(key)

# This thread will listen for incoming messages and add the keys to the list
listenThread = threading.Thread(target=listenForUDP)

# Start listening and responding to key request
listenThread.start()
lastMS = time.time()
while True:
    # Press the key inside the list
    for key in toBePressed:
        keyDown(key)
        print("pressed", key)
        toBePressed.remove(key)
        pressed.append((key, time.time()))
    
    # Check if there are keys to be released
    for touple in pressed:
        if (time.time() - touple[1] >= DELAY):
            keyUp(touple[0])
            pressed.remove(touple)
            print("released", key)


    lastMS = time.time()
