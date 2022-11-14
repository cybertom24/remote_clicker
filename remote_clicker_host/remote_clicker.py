"""
Remote Clicker Host
This script hosts an UDP Server and will press for DELAY seconds the keys passed asa letters via the UDP datagrams
"""


import socket
from pyautogui import keyDown, keyUp
import time
from threading import Thread

# Options:
PORT = 4000
#IP = socket.gethostbyname(socket.gethostname())
#IP = "192.168.137.1"
IP = "127.0.0.1"
DELAY = 0.10

# ------------------------------------------------------------------------------------

BUFFER_SIZE = 32
KEYS = "abcdefghijklmnopqrstuvwxyz1234567890"

# ------------------------------------------------------------------------------------

# Create the UDP Server and host it
receiveSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the address and port
serverAddress = (IP, PORT)
receiveSocket.bind(serverAddress)
print("Listening on", serverAddress)

# ------------------------------------------------------------------------------------

# Functions for the threads:
# This is the function that will be called when a key needs to be pressed
def pressKey(key):
    keyDown(key)
    time.sleep(DELAY)
    keyUp(key)

listen = True
# This is the function that checks if a datagram has been received and starts the threads for pressing the key
def listenerUDP():
    while listen:
        data, address = receiveSocket.recvfrom(BUFFER_SIZE)
        key = data.decode('utf-8')[0]
        
        print("pressed", key)
        Thread(target=pressKey, args=(key, )).start()

# ------------------------------------------------------------------------------------
        
if __name__ == "__main__":
    print("!! Use CTRL-C or write 'stop' to exit the program !!")
    
    # Start the listener thread
    listenThread = Thread(target=listenerUDP)
    # Set the listenThread as daemon so it will be killed when the program exits
    listenThread.daemon = True
    listenThread.start()

    # Hold the terminal until "stop" is written
    while input() != "stop":
        continue

    # Stop the thread and exit the program
    print("Exting program...")
    listen = False
    exit(0)