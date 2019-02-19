#!/usr/bin/env python3

import sys

#map pick locations to needle numbers; customize for your current warping:
locations = []
for i in range(117, 148):
	locations.append(i)
for i in range(148+1, 240):
	locations.append(i+1)
assert(len(locations) == 122)

if len(sys.argv) != 2:
	sys.exit('Usage:\n\tsend-pick.py <picks.txt>\n where each line of picks.txt looks like \'00110101000101010...00101\', with exactly ' + str(len(locations)) + ' digits in the line.')

picks = []
with open(sys.argv[1], 'r') as f:
	for line in f:
		pick = line.strip()
		if len(pick) != len(locations):
			sys.exit("ERROR: file has a line of length " + str(len(pick)) + " -- want all to be " + str(len(locations)))
		picks.append(pick)

from jacq3g import *

print("opening connection...")

loom = Jacq3G()
connection = Comm()

print("initializing connection...")

if not connection.initialize():
	sys.exit('Connection failed to initialize')
print("connection initialized")

for pick in picks:
	for i in range(0,len(pick)):
		if pick[i] == '1':
			loom.setPick(locations[i], True)
			pick += '1'
		else:
			loom.setPick(locations[i], False)
			pick += '0'

	print("Sending '" + pick + "'...")

	result = connection.send(loom.getPick())
	if not result:
		connection.shutdown()
		sys.exit('Failed to send pick')

print("shutting down...")
connection.shutdown()
