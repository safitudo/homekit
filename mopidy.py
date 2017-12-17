
import time
import json
import requests
import serial


removeTracklist = {"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.clear"};
shuffle = {"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.shuffle"};
play = {"jsonrpc": "2.0", "id": 1, "method": "core.playback.play"};


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


keypadNumbers = {
1: "vivaldi",
2: "topclassic",
3: "europetop",
4: "globaltop",
5: "breakfast",
6: "motivation",
7: "russian1",
8: "russian2",
9: "softrock",
10: "reggae",
11: "rock",
12: "electrovan",
13: "electro"}


def uri_payload(uri):
    return  {"jsonrpc": "2.0", "id": 1, "method": "core.tracklist.add", "params": {"uri": uri} };

def request_mopidy(payload):
    return requests.post('http://localhost:6680/mopidy/rpc', data = json.dumps(payload))

r = request_mopidy(removeTracklist)

r1 = request_mopidy(uri_payload(playlists["reggae"]));
shuffleR = request_mopidy(shuffle)

r2 = request_mopidy(play);
        
print r2.json();
