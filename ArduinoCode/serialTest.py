import serial

ser = serial.Serial(port='COM3', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=2)

try:
    ser.isOpen()
except:
    print("Error")
    exit()

if(ser.isOpen()):
    try:
        while(1):
            temp = ser.readline()[:-5]
            moisture = ser.readline()[-5:-2]
            print("Temp: ", temp)
            print("Moist: ", moisture)
    except Exception:
        print("Error")
else:
    print("Connection failed!")