import serial
import time

def sendData(element):
    print(element)
    serialcomm = serial.Serial('/dev/ttyACM0', 9600)

    serialcomm.timeout = 1

    while True:

        i = element.strip()

        serialcomm.write(i.encode())

        time.sleep(0.5)

        a = serialcomm.readline().decode('ascii')
        if len(a) > 0:
            break;

    serialcomm.close()

