import serial

class Sonar():
    
    def __init__(self, portname, baudrate):
        self.portname = portname
        self.baudrate = baudrate
        self.ser = serial.Serial(self.portname, self.baudrate, timeout = 1) 
    


    def getDistance(self):
        line = self.ser.readline()
        if line:
            string = line.decode()
            value = string.strip()
        self.ser.close()
        return float(value)