import serial
from database import Value, DatabaseManager

dbm = DatabaseManager("test")
ser = serial.Serial(port='COM3', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=2)

try:
    ser.isOpen()
except:
    print("Error")
    exit()

if(ser.isOpen()):
    try:
        while(1):
            temp = float(ser.readline()[:-5])
            moisture = float(ser.readline()[-5:-2])
            print("Temp: ", temp)
            print("Moist: ", moisture)
            object1 = Value(moisture, temp)
            dbm.add_to_db(object1)
    except Exception:
        print("Error")
else:
    print("Connection failed!")