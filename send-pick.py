#!/usr/bin/env python3

import sys

#map pick locations to needle numbers; customize for your current warping:
locations = []
for i in range(117, 138):
	locations.append(i)
for i in range(138+1, 240):
	locations.append(i)
assert(len(locations) == 122)

if len(sys.argv) != 2 or len(sys.argv[1]) != len(locations):
	sys.exit('Usage:\n\tsend-pick.py <00110101000101010...00101>\n NOTE: expecting exactly ' + str(len(locations)) + ' digits in pick.')

from jacq3g import *

loom = Jacq3G()
connection = Comm()

if not connection.initialize():
	sys.exit('Connection failed to initialize')

for i in range(0,len(argv[1])):
	if argv[1][i] == '1':
		loom.setPick(locations[i], True)

if not connection.send(loom.getPick()):
	connection.shutdown()
	sys.exit('Failed to send pick')

connection.shutdown()
