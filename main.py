import serial
import time
import pickle

ser = serial.Serial("/dev/tty.usbserial-A50285BI", baudrate=9600, parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=None)

startup = []
batch = []
start = time.time()
while len(startup) < 20:
    rx = ser.read()
    batch.append({'byte': rx, 'time': time.time() - start})
    if len(batch) > 1:
        if batch[-1]['time'] - batch[-2]['time'] > 0.05:
            bytes = [b['byte'] for b in batch]
            print(bytes)
            startup.append(batch.copy())
            batch.clear()

print('Startup recorded!')
print(startup)
file = open('startup_pickle', 'wb')
pickle.dump(startup, file)
file.close()

