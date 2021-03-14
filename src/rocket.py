#classes for LibreRocket
# all classes which store components have a getData method which returns a dict, which is then saved to a file by Rocket.SaveJson(self, path)
import json
class Rocket(object):
    "the main class for rocket files, has the method to actually save the file"
    parts: list #stores the list of the rocket's components
    def __init__(self,Filename,Parts=[]):
        self.parts=Parts
        self.filename = Filename
    def SaveJson(self, path:str):
        data={
            "filename":self.filename,
            "type":__name__,
            "parts":[]
        }
        for item in self.parts:
            data['parts'].append(item.getData()) #add each component to json parts list
        with open(str(path),'w+') as f:
            f.write(json.dumps(data,indent=4))
            f.close()
def loadJsontoObject(filename:str) -> Rocket:
    "loads a json file and returns the proper objects"
    with open(filename,"r") as f: #open file
        data = json.load(f) #read file
        for key in data['parts']:
            print(key['type'])
class fileParent(object):
    "The top level class for the file"
    def __init__(self,Name: str):
        self.name = Name
    def getData(self) -> str:
        return {
            'name':self.name,
            'type':__name__
        }
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
    parent = '' #contains the parent for a component, used in rendering treeview 
class motor(component):
    objtype=__name__
    "Fields for motors"
    def __init__(self,Name: str, Itot: float, Diameter: float, Mass: float, Length: float, Curve: dict,Material: str, Parent = ''):
        "Moves data into the correct areas"
        self.name = Name
        self.parent = Parent
        self.Itot = Itot
        self.material = Material
        self.diameter = Diameter
        self.mass = Mass
        self.length = Length
        self.curve = Curve
    def getData(self):
        return {
            "name":self.name,
            "parent":self.parent,
            "type":__name__,
            "data":{
                "mass":self.mass,
                "length":self.length,
                "diameter":self.diameter,
                "length":self.length,
                "material":self.material,
                "Itot":self.Itot,
            }
        }
class tube(component):
    "fields for any tube component in a rocket"
    objtype='tube'
    def __init__(self,Name: str, Mass: float, Length: float, Diameter: float, WallTh: float, Parent = ''):
        self.name = Name
        self.parent = Parent
        self.mass = Mass
        self.diameter = Diameter
        self.length = Length
        self.WallTh = WallTh
    def getData(self):
        return {
            "name":self.name,
            "type":__name__,
            "parent":self.parent,
            "data":{
                "mass":self.mass,
                "length":self.length,
                "diameter":self.diameter,
                "WallTh":self.WallTh
            }
        }
class nosecone(component):
    def __init__(self, Name: str, Generator: int, Mass: float, Length: float, Shoulder: bool, ShoulderDiameter: float):
        self.name = Name
        self.mass = Mass
        self.generator = Generator
        self.length = Length
        self.shoulder = Shoulder
        self.shoulderdiameter = ShoulderDiameter
    def getData(self):
        return {
            "name":self.name,
            "type":__name__,
            "parent":self.parent,
            "data":{
                "mass":self.mass,
                "length":self.length,
                "diameter":self.diameter,
                "generator":self.generator,
                "shoulder":self.shoulder
            }
        }
class trapfins(component):
    "automatc trapesoidal fins"
class ellipfins(component):
    "automatic ellptical fins"
class freefins(component):
    def __init__(self,Name: str, Points: dict):
        self.name = Name
        self.points = Points
    "freeform fins"