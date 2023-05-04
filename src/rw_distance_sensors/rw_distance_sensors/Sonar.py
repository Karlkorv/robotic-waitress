import serial

def main():
    sonar = Sonar('/dev/ttyACM01', 9600)
    while True:
        sonar.getDistance()

class Sonar():
    
    def __init__(self, portname, baudrate):
        self.portname = portname
        self.baudrate = baudrate
        # Timeout is for how long the Pi will wait for data before returning when reading
        try:
            self.ser = serial.Serial(self.portname, self.baudrate, timeout=10)
        except serial.SerialException as e:
            print(f"Error: Failed to open serial port {self.portname} with baud rate {self.baudrate}: {e}")
    


    def getDistance(self):
        sensorvals = None
        if not self.ser.is_open:
            self.ser.open()

        try:
            byte_data = self.ser.readline() # Accepts a byte string in utf-8 encoding
            sensorvals = byte_data.decode('utf-8').rstrip() # removes trailing whitespace and decodes from utf-8 to normal string
        except UnicodeDecodeError:
            self.ser.flushInput() # if there is something wrong with the input (e.g. misaligned newlines)
        self.ser.close()
        return sensorvals
    
    

if __name__ == '__main__':
    main()