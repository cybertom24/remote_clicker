"""
This is the main file for the app.
This app will send a UDP packet whenever the user touches the screen
A program on the host computer will receive the packet and press the corresponding key
This will be done in the quickest way possible
"""

# -------------------------------
# OPTIONS
HOST_IP = "192.168.1.86"
HOST_PORT = 4000
KEY = 'a'
# -------------------------------


from kivy.app import App
from kivy.uix.widget import Widget
import socket

# ----------------------------------------------------------

# UDP:
# Create a socket to send the keys on
sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def send(message):
    sendSocket.sendto(bytes(message, "utf-8"), (HOST_IP, HOST_PORT))
    return

# -----------------------------------------------------------

# Kivy:
class Screen(Widget):
    def on_touch_down(self, touch):
        send(KEY)        

class RemoteClickerApp(App):
    def build(self):
        return Screen()

# ------------------------------------------------------------

# Main:
if __name__ == '__main__':
    RemoteClickerApp().run()