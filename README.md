# loom
A tiny driver to talk to the AVL Jacq3 loom over usb-serial connection

```python
connection = Comm()  # sets up a usb-serial connection
connection.initialize() 
 
loom = Jacq3() # holds data that can be sent using Comm()
 
for i in range(0, loom.length, 4):
  loom.setPick(i, True) # pick i
 
connection.send(loom.getPick()) #send data over, press foot pedal to engage

connection.send(loom.getNullPick()) #clear all picks

connection.shutdown()
```

todo : Move Comm, Jacq3 in one class? Some helpers for binary patterns ? More documentation ?
 
