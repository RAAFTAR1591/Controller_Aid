These are the python files.<br>

ser = s.Serial('/dev/ttyACM1', 9800, timeout=1)<br>

Here "/dev/ttyACM1" must be changed according to the machine. These are the ports for my machine, it may not match with other machines.<br>

They can be found from Arduino IDE.<br>

os_test.py checks the system for Linux or Windows. This can also be implemented for detection of kernel. <br>

functions can be changed according to liking from the functions.py code. The key bindings can be changed according to our liking. <br>
