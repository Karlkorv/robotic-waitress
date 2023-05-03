import serial

def main():
    sonar = Sonar('/dev/ttyACM01', 9600)
    while True:
        #time.sleep(1)
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
        #sensorvals = self.ser.readline().decode('utf-8').rstrip()
        try:
            byte_data = self.ser.readline()
            print(byte_data)
            sensorvals = byte_data.decode('utf-8').rstrip()
        except UnicodeDecodeError:
            self.ser.flushInput()
            print("Flushar input")

        self.ser.close()
        return sensorvals
    
    

if __name__ == '__main__':
    main()