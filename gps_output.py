import serial
import time
import string
import pynmea2

print("start")

def get_coods():
	while True:
		port='/dev/ttyAMA0'
		ser=serial.Serial(port, baudrate=9600, timeout=0.5)
		dataout=pynmea2.NMEAStreamReader()
		newdata=ser.readline()
		try:
			msff = str(newdata, 'utf-8')
			gps_=pynmea2.parse(msff)
			gps='Latitude='+(str(gps_.latitude)[:8]) + ' & Longitude=' +(str(gps_.longitude)[:8])
			return gps
		except:
			pass
if __name__ == '__main__':
	data = get_coods()
	print(data)

