#classes for LibreRocket
# all classes which store components have a getJson method which returns a json string
import json
class component(object):
    "Basic fields for all components"
    name: str
    
    mass: float
    diameter: float
    length: float
    position: float
class motor(component):
    "Fields for motors"
    def __init__(self, Itot: float, Diameter: float, Mass: float, Length: float, Curve: dict):
        #Moves data into the correct areas
        self.Itot = Itot
        self.diameter = Diameter
        self.mass = Mass
        self.length = Length
        self.curve = Curve
class tube(component):
    def __init__(self, Mass: float, Length: float, WallTh: float):
        self.mass = Mass
        self.length = Length
        self.WallTh = WallTh
    def getJson(self):
        dict = {
            "mass":self.mass,
            "length":self.length,
            "WallTh":self.WallTh
        }
        return json.dumps(dict)