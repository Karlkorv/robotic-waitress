import serial
import struct

class Sonar():
    
    def __init__(self, portname, baudrate):
        self.portname = portname
        self.baudrate = baudrate
        # Timeout is for how long the Pi will wait for data before returning when reading
        self.ser = serial.Serial(self.portname, self.baudrate, timeout = 1)
    


    def getDistance(self):
        if self.ser.in_waiting > 0:
            data = self.ser.read(7)
            leftSonar, centerSonar, rightSonar = struct.unpack('>iii', data)
        self.ser.close()
        return (leftSonar, centerSonar, rightSonar)

    def closePort(self):
        self.ser.close()