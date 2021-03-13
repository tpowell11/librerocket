#classes for LibreRocket
# all classes which store components have a getJson method which returns a json string
import json
usedIds = [] #stores all used hexadecimal ids
class Rocket(object):
    "the main class for rocket files, has the method to actually save the file"
    parts: list #stores the list of the rocket's components
    def __init__(self,Filename,Parts=[]):
        self.parts=Parts
        self.filename = Filename
    def SaveJson(self,path: str):
        "dumps json of the file, then saves to the specified path"
        j = ''
        for item in self.parts:
            if type(item) == list:
                for ite in item:
                    j += ite.getJson()
                del item
        data = {
            "filename":self.filename,
            "parts":j + str(self.parts.getJson())
        }
        with open(str(path),'w+') as f:
            f.write(json.dumps(data))
            f.close()
            
class fileParent(object):
    "The top level class for the file"
    def __init__(self,Name: str):
        self.name = Name
    def getJson(self) -> str:
        data = {
            'name':self.name
        }
        return json.dumps(data)
class stage(object):
    "class for rocket stages"
    def __init__(self, Name: str):
        self.name = Name
class component(object):
    "Basic fields for all components"
    name: str
    mass: float
    diameter: float
    length: float
    position: float
    material: str #refers to a material in materials.json
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
        data = {
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
        return json.dumps(data)
class tube(component):
    objtype='tube'
    def __init__(self,Name: str, Mass: float, Length: float, Diameter: float, WallTh: float):
        self.name = Name
        self.mass = Mass
        self.diameter = Diameter
        self.length = Length
        self.WallTh = WallTh
    def getJson(self):
        data = {
            "name":self.name,
            "type":'tube',
            "data":{
                "mass":self.mass,
                "length":self.length,
                "diameter":self.diameter,
                "WallTh":self.WallTh
            }
        }
        return json.dumps(data)
class nosecone(component):
    def __init__(self, Name: str, Generator: int, Mass: float, Length: float, Shoulder: bool, ShoulderDiameter: float):
        self.name = Name
        self.mass = Mass
        self.generator = Generator
        self.length = Length
        self.shoulder = Shoulder
        self.shoulderdiameter = ShoulderDiameter
class trapfins(component):
    "automatc trapesoidal fins"
class ellipfins(component):
    "automatic ellptical fins"
class freefins(component):
    def __init__(self,Name: str, Points: dict):
        self.name = Name
        self.points = Points
    "freeform fins"