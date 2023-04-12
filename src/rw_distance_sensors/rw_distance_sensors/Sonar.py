import serial
class Sonar():
    
    def __init__(self, portname, baudrate):
        self.portname = portname
        self.baudrate = baudrate
        self.ser = serial.Serial(self.portname, self.baudrate, timeout = 1) 
    


    def getDistance(self):
        value = None
        line = self.ser.readline()
        if line:
            value = line.decode()
        return value

    def closePort(self):
        self.ser.close()