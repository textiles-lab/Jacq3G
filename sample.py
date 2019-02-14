from jacq3g import *

loom = Jacq3G()
connection = Comm()

print('loom length: ', loom.length())

print( 'initialize:', connection.initialize())

#pick every 4th
for i in range(0,360,4):
    loom.setPick(i, True)

data = loom.getPick()

print('send: ', connection.send(data))

#unset everything
data = loom.getNullPick()

print('send: ', connection.send(data))


print('shutdown')
connection.shutdown()
