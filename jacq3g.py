#!/usr/bin/env python3
import serial
import time
def toBits(arr):
    out = []
    arr = arr + []
    while len(arr) % 7 > 0:
        arr.append(False)
        while len(arr) >= 7:
            out.append( arr[0] << 6 | arr[1] << 5 | arr[2] << 4 | arr[3] << 3 | arr[4] <<  2 | arr[5] << 1 | arr[6] )
            arr = arr[7:]
    assert(len(arr) == 0)
    return bytearray(out)

class Jacq3G:
    def __init__(self):
        self.frames = [False] * 360

    def length(self):
        return len(self.frames)

    def clearFrame(self):
        self.frames = [False] * 360

    def setPick(self, index, is_up):
        self.frames[index] = is_up

    def getPick(self):
        pick = b'\x80' + toBits(self.frames[0:120]) + b'\xc0' + b'\x81' + toBits(self.frames[120:240]) +       b'\xc0' + b'\x82'+toBits(self.frames[240:360])+b'\xc0';
        return pick

    def getNullPick(self):
        pick = b'\x80' + toBits([False]*120) + b'\xc0' +  b'\x81' + toBits([False]*120) +  b'\xc0' +  b'\x82' + toBits([False]*120) + b'\xc0';
        return pick


class Comm:
    # better port identification
    def __init__(self):
        self.port = "COM4"
        self.serial =  serial.Serial(port=self.port, baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)

    def initialize(self):
        if self.serial.isOpen() == False:
            return False
        self.serial.reset_input_buffer()
        self.serial.reset_output_buffer()
        self.serial.write(b'\xc3')
        response = self.serial.read(1)
        self.ok = True
        return  (response == b'\xc3')

    def send(self, data):
        #if self.ok:
        #    self.serial.write(data)
        #    self.ok = False
        while True:
            got = self.serial.read(1)
            if len(got) == 0: continue
            if got == b'a':
                self.serial.write(data)
                self.ok = False
            if got == b'b':
                self.serial.write(b'\xc1') #de-activate
                self.ok = True
                break
        return self.ok

    def shutdown(self):
        self.serial.close()



