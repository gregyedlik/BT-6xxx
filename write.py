import serial
import time
import pickle

ser = serial.Serial("/dev/tty.usbserial-A50285BI", baudrate=9600, parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=None)

file = open('startup_pickle', 'rb')
startup = pickle.load(file)
file.close()

start = time.time()
for batch in startup:
    while time.time() - start < batch['time']:
        time.sleep(0.001)
    for b in batch['data']:
        ser.write(b)
        time.sleep(0.0001)
    print(batch['data'])

print('Startup done')

while 1:
    start = time.time() - startup[-5]['time']
    for batch in startup[-4:]:
        while time.time() - start < batch['time']:
            time.sleep(0.001)
        for b in batch['data']:
            ser.write(b)
            time.sleep(0.0001)
        print(batch['data'])
