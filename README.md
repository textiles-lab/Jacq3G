# Jacq3G
A tiny driver to talk to the AVL Jacq3 loom over usb-serial connection

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

## send-pick

Send-pick is a small utility that uses Jacq3G to send a single pick (passed as a string of ones and zeroes on the command line) to the loom. You can use it (along with various other shell utilities) to easily pipe patterns to the loom:

```
cat twill.txt | xargs -n1 ./send-pick.py
```

## TODO
todo : Move Comm, Jacq3 in one class? Some helpers for binary patterns ? More documentation ?
 
