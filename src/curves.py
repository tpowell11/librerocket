# Functions and classes to work with standard model rocketry thrustcurves
import requests #thrustcurve interaction
import json #json parse
from lxml import etree #xml parse
from matplotlib import pyplot as plt #used in visualization methods
import rocket
with open("../cfg/tcapi.json") as f:
    pass
    #cfg = json.load(f)#load the config json
with open("../db/motors.json") as f:
    motorsdb = json.load(f)#load the motors database
def TCsearch(CommonName:str,Designation:str=None,Iclass:str=None,Diameter:int=None,):
    "search Thrustcuve.org for a motor"
    json = {
        "designation":Designation if type(Designation)!=None else '',
        "commonName":CommonName,
        "impulseClass":Iclass if type(Iclass)!=None else '',
        "diameter":Diameter if type(Diameter)!=None else '',
        "hasDataFiles":True,
        "maxResults":20
    }
    data = requests.post("https://www.thrustcurve.org/api/v1/search.json",json=json)
    print(data.text)
    #results = json.loads(data)
    #print(results)
TCsearch("C6")
class ENGfile(object):
    "contains the data from a RASP .eng file"
    def __init__(self, filename):
        "pull file contents into object"
        with open(filename) as f:
            root=etree.parse(f)
            self.timeSeries = []
            self.forceCurve = []
            self.massCurve = []
            self.cgCurve = []
            #getting params from the 'enginge' xml tag's attributes
            self.atrrib:dict = root.find('//engine').attrrib
            for item in root.iter('eng-data'):
                #loop through datapoints and add them to lists
                self.timeSeries.append(float(item.get('f')))
                self.forceCurve.append(float(item.get('f')))
                self.massCurve.append(float(item.get('m')))
                self.cgCurve.append(float(item.get('cg')))
    def plot(self):
        "plot the points in the file with matplotlib for wasy visualization"
        self._fig,self._axs=plt.subplots(3)

        self._axs[0].plot(self.timeSeries,self.forceCurve)
        self._axs[0].set_xlabel('Time (seconds)')
        self._axs[0].set_ylabel('Force (sewtons)')

        self._axs[1].plot(self.timeSeries,self.massCurve)
        self._axs[1].set_xlabel('Time (seconds)')
        self._axs[1].set_ylabel('Mass (grams)')

        self._axs[2].plot(self.timeSeries,self.cgCurve)
        self._axs[2].set_xlabel('Time (seconds)')
        self._axs[2].set_ylabel('Center of Gravity (mm)')
        plt.show()
    def generateMotor(self,Name,Parent='',Position=0.0)->rocket.motor:
        "returns a rocket.motor() object"
        return rocket.motor(Name,self.atrrib['Itot'],self.atrrib['dia'])

from lxml import etree

with open('AeroTech_F39T.eng') as f:
    root=etree.parse(f)
    f=[]
    t=[]
    m=[]
    cg=[]
    fig, axs = plt.subplots(2)

    for item in root.iter('eng-data'):
        f.append(float(item.get('f')))
        m.append(float(item.get('m')))
        cg.append(float(item.get('cg')))
        t.append(float(item.get('t')))
    axs[0].plot(t,f)
    axs[1].plot(t,m)
    plt.show()
    