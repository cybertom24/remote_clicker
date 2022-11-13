# remote_clicker
A simple python script to press a keyboard key by tapping the screen on a smartphone. iOS and Android compatible.
Use this project to play some games which require to press only one key.
You can connect as many smartphone as you like, but there are only 26 (letters) + 10 (numbers) keys available.


Requirements:
- Python installed on the host machine
- A python IDE installed on the smartphone with Kivy library
- Both host and smartphone need to be on the same LAN


Instructions:

1) Clone the repository on the host machine 
2) Execute the python script inside the directory "remote_clicker_host" by opening window's terminal (cmd or powershell) inside the directory and using the command "python ./remote_clicker.pyù
3) Download on the smartphone the folder "remote_clicker_app"
4) Open the "main.py" file with a python IDE on the smartphone
5) Be sure that the host computer and the smartphone are connected to the same LAN
6) Modify the "HOST_IP" variable inside the main.py script and set it to the IP that has been printed on the terminal by the "remote_clicker.py" script
7) Set the "KEY" variable to whatever LOWER_CASE letter or number you like
8) Start the main.py script


Usage:
Tap the screen on the smartphone to send a (UDP) message to the host computer with the key to be pressed. The host will then press the desired key holding it down for DELAY (default 0.1) seconds.