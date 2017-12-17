import time
import json
import requests
import serial
import time

# time.sleep(10)

digits_time = time.time()
digits = ""

print("Starting program")


keypadNumbers = {
	"101": "vivaldi",
	"102": "topclassic",
	"103": "europetop",
	"104": "globaltop",
	"105": "breakfast",
	"106": "motivation",
	"107": "russian1",
	"108": "russian2",
	"109": "softrock",
	"110": "reggae",
	"111": "rock",
	"112": "electrovan",
	"113": "electro"
}

playlists = {"vivaldi" : "spotify:user:elo3k7fqv2narpyl6ttr4j93q:playlist:6BJtQHjOMxcpUsYbR988k6",
"globaltop": "spotify:user:pcnaimad:playlist:01wmKsbuDlSR5Lv1guyie8",
"europetop": "spotify:user:21ifzjxggdajdpc4w6iqxslkq:playlist:1xlPS15OnQus2owduj1sTh",
"topclassic": "spotify:user:rogeriotutti:playlist:2shU0q1gKzX4dwpYkLFrPw",
"motivation": "spotify:user:warnerfrspotify:playlist:7igLXKeTEFY63fMiI0Oj8i",
"breakfast": "spotify:user:connemaralake:playlist:4ySX5SuVzj3P7z4Ct9UsJG",
"russian1": "spotify:user:11156468774:playlist:35UxXEx0IWrB1H8zS404E9",
"russian2": "spotify:user:moacyrsalim:playlist:6D6QKSCArtoe7UUwNntW0O",
"softrock": "spotify:user:elo3k7fqv2narpyl6ttr4j93q:playlist:7eZF0GaJcwSuqJ2aPSCzYZ",
"reggae": "spotify:user:elo3k7fqv2narpyl6ttr4j93q:playlist:7L6sjUExEPr0JeXofrGUYU",
"rock": "spotify:user:elo3k7fqv2narpyl6ttr4j93q:playlist:07OdnGnYsFdDNpMTgJq6yK",
"electrovan": "spotify:user:elo3k7fqv2narpyl6ttr4j93q:playlist:5QvBWhLTooNsc61srsyXYb",
"electro": "spotify:user:elo3k7fqv2narpyl6ttr4j93q:playlist:66ai80lOCiEjLGAq9fllVn"}

def uri_payload(uri):
    return  {"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.add", "params": {"uri": uri} };

def request_mopidy(payload):
    return requests.post('http://localhost:6680/mopidy/rpc', data = json.dumps(payload))


ser = serial.Serial('/dev/ttyACM0', 9600)
# ser = serial.Serial('/dev/tty.usbmodem1421', 9600)

r = requests.get('http://192.168.0.2/api/3LvqZztMKdWDKQUGOLzrdTZdhiqQHNR80CVkPP9K/lights')
# print r.json()
lights = r.json()
for val in lights:
	print val,lights[val]
while True:
	line = ser.readline()

	if (len(line)==3):
		ts = time.time()
		if ( ts - digits_time > 10 ):
			digits = str(line[:1])
		else:
			digits += str(line[:1])
			if (len(digits)==3 and digits in keypadNumbers):
				uri = playlists[keypadNumbers[digits]]
				print "keypad: ", keypadNumbers[digits], uri
				
				r = request_mopidy(removeTracklist)
				r1 = request_mopidy(uri_payload(uri));
				shuffleR = request_mopidy(shuffle)
				r2 = request_mopidy(play);
				        
				print r2.json();
				
				digits = ""


		digits_time = ts
	
	
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
