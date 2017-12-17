import time
import json
import requests
import serial

time.sleep(10)

print("Starting program")

ser = serial.Serial('/dev/ttyACM0', 9600)
r = requests.get('http://192.168.0.2/api/3LvqZztMKdWDKQUGOLzrdTZdhiqQHNR80CVkPP9K/lights')
# print r.json()
lights = r.json()
for val in lights:
	print val,lights[val]
while True:
	line = ser.readline()
	if (line[:3] == "GON" or line[:7] == "GONDOOR"):
		print "On process started"
		payload = {"on": True}
		for val in lights:
			# print val,lights[val]
			rr = requests.put('http://192.168.0.2/api/3LvqZztMKdWDKQUGOLzrdTZdhiqQHNR80CVkPP9K/lights/'+val+'/state', data = json.dumps(payload))
	if (line[:4] == "GOFF"):
		print "OFF process started"
		payload = {"on": False}
		for val in lights:
			# print val,lights[val]
			rr = requests.put('http://192.168.0.2/api/3LvqZztMKdWDKQUGOLzrdTZdhiqQHNR80CVkPP9K/lights/'+val+'/state', data = json.dumps(payload))

# /api/3LvqZztMKdWDKQUGOLzrdTZdhiqQHNR80CVkPP9K/lights/3/state
# 3LvqZztMKdWDKQUGOLzrdTZdhiqQHNR80CVkPP9K
# http://192.168.0.2/api/3LvqZztMKdWDKQUGOLzrdTZdhiqQHNR80CVkPP9K/lights
