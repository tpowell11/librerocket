import requests
import json
import rocket
with open("../cfg/tcapi.json") as f:
    cfg = json.load(f)#load the config json
with open("../db/motors.json") as f:
    motorsdb = json.load(f)#load the motors database
    
#print(cfg["TCsearch"])
def getTcMetadata():
    "gets the search params from thrustcurve.org"
def getCurve():
    "downloads a motor curve from thrustcurve.org"
    requests.get(cfg["TCdownload"]).json()#download the curve