#classes for LibreRocket
# all classes which store components have a getJson method which returns a json string
import json
import random #provides random hex IDs
usedIds = [] #stores all used hexadecimal ids
class component(object):
    "Basic fields for all components"
    name: str
    mass: float
    diameter: float
    length: float
    position: float
class motor(component):
    objtype='motor'
    "Fields for motors"
    def __init__(self,Name: str, Itot: float, Diameter: float, Mass: float, Length: float, Curve: dict):
        #Moves data into the correct areas
        self.name = Name
        self.Itot = Itot
        self.diameter = Diameter
        self.mass = Mass
        self.length = Length
        self.curve = Curve
    def getJson(self):
        dict = {
            "name":self.name,
            "type":'motor',
            "data":{
                "mass":self.mass,
                "length":self.length,
                "diameter":self.diameter,
                "length":self.length,
                "Itot":self.Itot,
            }
        }
class tube(component):
    objtype='tube'
    def __init__(self,Name: str, Mass: float, Length: float, Diameter: float, WallTh: float):
        self.name = Name
        self.mass = Mass
        self.diameter = Diameter
        self.length = Length
        self.WallTh = WallTh
    def getJson(self):
        dict = {
            "name":self.name,
            "type":'tube',
            "data":{
                "mass":self.mass,
                "length":self.length,
                "diameter":self.diameter,
                "WallTh":self.WallTh
            }
        }
        return json.dumps(dict)
class nosecone(component):
    def __init__(self, Name: str, Generator: int, Mass: float, Length: float, Shoulder: bool, ShoulderDiameter: float):
        self.name = Name
        self.mass = Mass