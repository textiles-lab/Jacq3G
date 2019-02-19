# Jacq3G
A tiny driver to talk to the AVL Jacq3 loom over usb-serial connection

Requires the 'pySerial' module.

```python
from jacq3g import *

connection = Comm()  # sets up a usb-serial connection
connection.initialize() 
 
loom = Jacq3G() # holds data that can be sent using Comm()
 
for i in range(0, loom.length, 4):
  loom.setPick(i, True) # pick i
 
connection.send(loom.getPick()) #send data over, press foot pedal to engage

connection.send(loom.getNullPick()) #clear all picks

connection.shutdown()
```

## send-picks

Send-picks is a small utility that uses Jacq3G to send picks from a file (containing, on each line, a string of ones and zeroes) to the loom. You can use it to easily pipe patterns to the loom:

```
./send-picks.py twill.txt
```

## TODO
todo : Move Comm, Jacq3 in one class? Some helpers for binary patterns ? More documentation ?
 
