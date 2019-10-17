#!/usr/bin/env python3

import sys

import png

#map pick locations to needle numbers; customize for your current warping:
locations = []
#for i in range(117, 170):
#	locations.append(i)
#for i in range(170+1, 240):
#	locations.append(i)
#assert(len(locations) == 122)

for i in range(120, 240):
	locations.append(i)
assert(len(locations) == 120)

if len(sys.argv) != 2:
	sys.exit('Usage:\n\tsend-pick.py <picks.txt or picks.png>\n If you pass a ".txt" file, each line should looks like \'00110101000101010...00101\', with exactly ' + str(len(locations)) + ' digits in the line.\n If you pass a ".png" file, each row of should have only black or white pixels, with exactly ' + str(len(locations)) + ' pixels in a line.')

picks = []

if sys.argv[1].endswith('.txt'):
	with open(sys.argv[1], 'r') as f:
		for line in f:
			pick = line.strip()
			if len(pick) != len(locations):
				sys.exit("ERROR: file has a line of length " + str(len(pick)) + " -- want all to be " + str(len(locations)))
			picks.append(pick)
elif sys.argv[1].endswith('.png'):
	(width, height, rows, info) = png.Reader(file=open(sys.argv[1], 'rb')).asRGB8()
	if width != len(locations):
		sys.exit("ERROR: file has a width of " + str(width) + " -- want width to be " + str(len(locations)))
	for row in rows:
		pick = ""
		for i in range(0,len(row),3):
			r = row[i+0]
			g = row[i+1]
			b = row[i+2]
			if r == 0 and g == 0 and b == 0:
				pick += "0"
			elif r == 255 and g == 255 and b == 255:
				pick += "1"
			else:
				sys.exit("ERROR: file contains a pixel with color " + str(r) + ", " + str(g) + ", " + str(b) + " -- want only black and white.")
		picks.append(pick)
else:
	sys.exit("ERROR: file does not end in '.txt' or '.png'")

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
