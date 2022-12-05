import serial
import time
import pickle

ser = serial.Serial("/dev/tty.usbserial-A50285BI", baudrate=9600, parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=None)

startup = []
batch = []
start = None
while len(startup) < 9:
    rx = ser.read()
    if start is None:
        start = time.time()
    batch.append({'byte': rx, 'time': time.time() - start})
    if len(batch) > 1:
        if batch[-1]['time'] - batch[-2]['time'] > 0.05:
            bytes = [b['byte'] for b in batch]
            print(bytes)
            startup.append({'time': batch[0]['time'], 'data': bytes})
            batch.clear()

print('Startup recorded!')
for b in startup:
    print(str(round(b['time'], 2)) + "\t" + str(b['data']))
file = open('startup_pickle', 'wb')
pickle.dump(startup, file)
file.close()

