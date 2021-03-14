#classes for LibreRocket
# all classes which store components have a getData method which returns a dict, which is then saved to a file by Rocket.SaveJson(self, path)
import json
import math
#
# main class
#
class Rocket(object):
    "the main class for rocket files, has the method to actually save the file"
    parts: list #stores the list of the rocket's components
    def __init__(self,Filename,Parts=[]):
        self.parts=Parts
        self.filename = Filename
    def SaveJson(self, path='.'):
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
    parts = []
    f = open(filename,"r") #open file
    print('test')
    data = json.load(f) #read file
    for key in data['parts']:
        typ = key['type']
        #print(typ)
        if typ == 'fileParent':
            parts.append(fileParent(key['name']))
        elif typ == 'motor':
            parts.append(motor(key['name'],key['data']['Itot'],key['data']['diameter'],
                                key['data']['mass'],key['data']['length'],key['data']['curve'],
                                key['parent']
                                ))
            print('found motor')
        elif typ == 'tube':
            parts.append(tube(
                key['name'],key['data']['mass'],key['data']['length'],key['data']['diameter'],key['data']['wallth'],key['parent']
            ))
            print('found tube')
        elif typ == 'nosecone':
            parts.append(nosecone(
                key['name'], key['data']['generator'],key['data']['mass'],key['data']['length'],key['data']['shoulder'],key['data']['shoulderDiameter']
            ))
            pass
        elif typ == 'trapfins':
            if key['data']['isTabbed'] == False:
                parts.append(trapfins(
                    key['name'],key['data']['finCount'],key['data']['finTop'],key['data']['finOuter'],
                    key['data']['finHeight'],key['data']['finBottom'],Parent = key['parent']
                ))
            else:
                parts.append(trapfins(
                    key['name'],key['data']['finCount'],key['data']['finTop'],key['data']['finOuter'],
                    key['data']['finHeight'],key['data']['finBottom'],Parent = key['parent'],
                    TabDst=key['data']['tabDst'],TabLength=['data']['tabLength'],TabHeight=key['data']['tabHeight']
                ))
        elif typ == 'ellipFins':
            pass
        elif typ == 'freeFins':
            pass
    return Rocket(filename,parts)
#
# File only classes
#
class fileParent(object):
    "The top level class for the file"
    def __init__(self,Name: str):
        self.name = Name
    def getData(self) -> str:
        return {
            'name':self.name,
            'type':type(self).__name__
        }
class stage(object):
    "class for rocket stages"
    def __init__(self, Name: str):
        self.name = Name
    def getData(self)->dict:
        return {
            "name":self.name
        }
#
# Classes that represent components
#
class component(object):
    "Basic fields for all components"
    name: str
    mass: float
    diameter: float
    length: float
    position: float
    material: str #refers to a material in materials.json
    parent = '' #contains the parent for a component, used in rendering treeview 
    def getDensity(self)->float:
        "gets the density of a material from the material db"
        with open('../db/materials.json','r') as f:
            db = json.load(f)
            return db['struct'][self.material]['density'] #look up the density in the db
    def getMass(self)->float:
        "returns the component's mass"
        return self.mass
    def getVolume(self)->None:
        pass
class motor(component):
    objtype=__name__
    "Fields for motors"
    def __init__(self,Name: str, Itot: float, Diameter: float, Mass: float, Length: float, Curve: dict, Parent = '', Position = 0.0):
        "Moves data into the correct areas"
        self.name = Name
        self.parent = Parent
        self.Itot = Itot
        self.diameter = Diameter
        self.mass = Mass
        self.length = Length
        self.curve = Curve
        self.position = Position
    def getData(self)->dict:
        return {
            "name":self.name,
            "parent":self.parent,
            "type":type(self).__name__,
            "data":{
                "mass":self.mass,
                "length":self.length,
                "diameter":self.diameter,
                "length":self.length,
                "Itot":self.Itot,
                "curve":self.curve
            }
        }
class tube(component):
    "fields for any tube component in a rocket"
    def __init__(self,Name: str, Mass: float, Length: float, Diameter: float, WallTh: float, Parent = '', isMotorHolder=False):
        self.name = Name
        self.parent = Parent
        self.mass = Mass
        self.diameter = Diameter
        self.length = Length
        self.WallTh = WallTh
        self.isMotorHolder = isMotorHolder
    def getData(self)->dict:
        return {
            "name":self.name,
            "type":type(self).__name__,
            "parent":self.parent,
            "data":{
                "mass":self.mass,
                "length":self.length,
                "diameter":self.diameter,
                "wallth":self.WallTh,
                "isMotorHolder":self.isMotorHolder
            }
        }
    def getSurfaceArea(self)->float:
        "returns the surface area of the tube"
        return 2*math.pi*(self.diameter/2)*(self.length+self.diameter/2)
    def getVolume(self)->float:
        "returns the volume of the component"
        return (math.pi*(self.diameter/2)**2)*self.length
    def getMass(self)->float:
        "returns the mass of the component"
        return self.getDensity()*self.getVolume()
class nosecone(component):
    def __init__(self, Name: str, Generator: int, Mass: float, Length: float, Shoulder: bool, ShoulderDiameter: float):
        self.name = Name
        self.mass = Mass
        self.generator = Generator
        self.length = Length
        self.shoulder = Shoulder
        self.shoulderdiameter = ShoulderDiameter
    def getData(self)->dict:
        return {
            "name":self.name,
            "type":type(self).__name__,
            "parent":self.parent,
            "data":{
                "mass":self.mass,
                "length":self.length,
                "generator":self.generator,
                "shoulder":self.shoulder,
                "shoulderDiameter":self.shoulderdiameter
            }
        }
class trapfins(component):
    "automatc trapesoidal fins"
    def __init__(self, Name: str,Thickness, FinCount: int, FinTop:float, FinOuter:float, FinHeight: float,FinBottom:float, Parent = '', IsTabbed=False, TabDst = 0, TabLength = 0, TabHeight = 0):
        self.name=Name
        self.thickness = Thickness
        self.finTop=FinTop
        self.finOuter=FinOuter
        self.finHeight=FinHeight
        self.finBottom=FinBottom
        self.parent=Parent
        self.finCount = FinCount
        if IsTabbed != False:
            self.isTabbed=IsTabbed
            self.tabDst=TabDst
            self.tabLength=TabLength
            self.tabHeight=TabHeight
        else:
            self.isTabbed = False
    def getArea(self)->float:
        "returns the area of the fin component"
        if self.isTabbed == False:
            return self.finHeight((.5*self.finTop)+(.5*self.finBottom)+self.finOuter)
        else:
            return self.finHeight((.5*self.finTop)+(.5*self.finBottom)+self.finOuter)+(self.tabHeight*self.tabLength)
    def getVolume(self)->float:
        "returns the component's volume"
        return self.getArea()*self.thickness
    def getMass(self)->float:
        "returns the component's mass"
        return self.getVolume()*self.getDensity()
    def getData(self)->dict:
        base = {
            "name":self.name,
                "type":type(self).__name__,
                "parent":self.parent,
                "data":{
                    "finCount":self.finCount,
                    "finTop":self.finTop,
                    "finOuter":self.finOuter,
                    "finHeight":self.finHeight,
                    "finBottom":self.finBottom,
                    "isTabbed":self.isTabbed
                }
            }
        if self.isTabbed == True:
            base['data']['tabDst'] = self.tabDst
            base['data']['tabLength'] = self.tabLength
            base['data']['tabHeight'] = self.tabHeight
            return base #retrun modified dict
        else:
            return base #retrun unmodified dict

class ellipfins(component):
    "automatic ellptical fins"
class freefins(component):
    def __init__(self,Name: str, Points: dict):
        self.name = Name
        self.points = Points
    "freeform fins"
class massComponent(component):
    def __init__(self, Mass: float, Diameter:float ,Positon:float, Parent = ''):
        self.mass = Mass
        self.diameter = Diameter
        self.parent = Parent
        self.position = Positon

    def getData(self)->dict:
        return {
            "name":self.name,
            "type":type(self).__name__,
            "parent":self.parent,
            "data":{
                "mass":self.mass,
                "length":self.length,
                "diameter":self.diameter,
                "position":self.position
            }
        }