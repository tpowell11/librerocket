import lxml #xml handling
import json #json handling
import zipfile #for working with the zipped xml
import rocket #main project classes
from io import bytes, TextIOWrapper #for type annotations
class rocketFile(object):
    """contains and manipulates OpenRocket (<=15.03) files
    """
    def openfile(self, filepath: str)->bytes or TextIOWrapper:
        "gets the IO object for a given file, should not be called outside of this class"
        self.filepath = filepath
        try:
            zf = zipfile.ZipFile(filepath,mode='r') #declare the actual file binary
            return zf.open('rocket.ork') #open the internal file from the zip
        except zipfile.BadZipFile:
            return open(filepath,'r')
            
    def parseORK(self,filepath: str)->list[dict]:
        """
        Loads both direct xml ork's and zipped xml ork (the default in openrocket)
        It returns a list of dicts. To find the type of the component that the values came from,
        access self.components[i:int]['cmptype']. This returns a string of the component's name
        """
        m=[]
        has_attributes = ['innertube','bulkhead','tubecoupler','masscomponent','nosecone','parachute','bodytube',
        'shockcord','freeformfinset','centeringring','motormount','streamer','trapezoidfinset','launchlug','ellipticalfinset',
        'transition','tubefinset','engineblock']
        #these lists define where specific elements are processed
        is_value_string=['finish','shape','masscomponenttype','designation','cd','deployevent','clusterconfiguration',
                        'clusterscale','clusterrotation']
        is_value_float=['length','thickness','aftradius','aftshoulderlength','aftshoulderthickness','mass',
                        'packedlength','packedradius','radialposition','radialdirection','radius','outerradius',
                        'diameter','delay','linelength','linecount','deploydelay','fincount','rotation','cant','tabheight'
                        'tablength','filletradius','striplength','stripwidth','packedlength','packedradius','deployaltitude',
                        'cordlength','tipchord','sweeplength','height','rootchord','foreradius','foreshoulderradius',
                        'foreshoulderlength','foreshoulderthickness','aftshoulderradius','aftshoulderlength',
                        'aftshoulderthickness']
        is_value_bool=['aftshouldercapped','foreshouldercapped','shapeclipped']
        is_material=['material','linematerial','filletmaterial']
        root=lxml.etree.parse(self.openfile(filepath))

        for element in root.iter('*'): #get all of the tags in the document
            if element.tag in has_attributes:
                m.append({'cmptype':element.tag}) #append the part's name to the list
            #general processing for elements whose data is stored in element text
            try:
                if element.tag in is_value_float:
                    m[-1][element.tag]=float(element.text)
                if element.tag in is_value_string: #make the element's payload a float
                    m[-1][element.tag]=str(element.text)
                if element.tag in is_value_bool: #make the element's payload a bool
                    m[-1][element.tag]=bool(element.text)
            except ValueError:
                m[-1][element.tag]=element.text #mostly for <sometag>auto</sometag>
            #special processing for elements that use XML attibutes or do not work with the above
            if element.tag == 'preset':
                m[-1][element.tag]={'mfg':element.get('manufacturer'),'pn':element.get('partno'),'hash':element.get('digest')}
            if element.tag == 'position':
                m[-1][element.tag]={'pos':float(element.text),'type':element.get('type')}
            if element.tag == 'motor':
                m[-1][element.tag]=element.get('configid')
            if element.tag == 'tabposition':
                m[-1][element.tag]={'pos':float(element.text),'rel':element.get('relativeto')}
            if element.tag in is_material:
                m[-1][element.tag]={'name':element.text,'type':element.get('type'),'density':float(element.get('density'))}
            if element.tag == 'finpoints':
                m[-1][element.tag]={} #finpoints are a group of attributes to the fins and need to be processed as such
            if element.tag == 'point':
                m[-1][-1][element.tag]={'x':element.get('x'),'y':element.get('y')} #group finpoints with their parent
        self.components=m
        self.importedfiletype='ork15' #annotate the object
    def parseRKT(self,filepath:str)->list[dict]:
        m=[]
        has_attributes = [
            'BodyTube','Ring','LaunchLug','FinSet','MassObject','Streamer','Parachute','NoseCone','Transition'
        ]
        is_value_float = [
            'KnownMass','Density','KnownCG','Xb','CalcMass','CalcCG','RadialLoc','RadialAngle','Len','WallThickness','BaseDia',
            'ShoulderLen','ShoulderOD','Dia','DragCoefficient','ShroudLineLength','ShroudLineMassPerMM','Width',
            'TabLength','TabDepth','TabOffset','RootChord','TipChord','SemiSpan','SweepDistance','CantAngle','OD','ID',
            'EngineOverhang','MotorDia','FrontShoulderLen','RearShoulderLen','FrontShoulderDia','RearShoulderDia','FrontDia',
            'RearDia'
        ]
        is_value_int = [
            'DensityType','LocationMode','FinishCode','SerialNo','ShapeCode','ConstructionType','ChuteCount','FinCount',
            'TipShapeCode','UsageCode'
        ]
        is_value_str = [
            'Material','ShroudLineMaterial'
        ]
        is_value_bool = [
            'UseKnownCG','IsMotorMount','IsInsideTube','AutoSize'
        ]
        f=open(filepath,'r')
        root=lxml.etree.parse(f)
        for element in root.iter('*'):
            if element.tag in has_attributes:
                m.append({'cmptype':element.tag}) #append the part's name to the list
            #general processing for elements whose data is stored in element text
            if element.tag in is_value_float:
                m[-1][element.tag]=float(element.text)
            if element.tag in is_value_int:
                m[-1][element.tag]=float(element.text)
            if element.tag in is_value_str: #make the element's payload a float
                m[-1][element.tag]=str(element.text)
            if element.tag in is_value_bool: #make the element's payload a bool
                m[-1][element.tag]=bool(element.text)
            if element.tag == 'PointList': #converts the <PointList>50,0|75.0,50.0|37,12|0.0,0.0|</PointList> to list[tuple]
                points = []
                try: 
                    for pair in element.text.split('|'): #split out each pair
                        j =tuple(map(float,pair.split(','))) #map each number to float type
                        points.append(j)
                except: #for .split's insistance on inserting a [...,''] in lists
                    pass
                m[-1][element.tag]=points
            self.components = m
            self.importedfiletype = 'rkt'
    def getJson(self):
        return json.dumps(self.components)
    def getRocket(self)-> rocket.Rocket:
        "gets a Rocket object from openrocket xml or rocksim xml"
        if self.importedfiletype == 'ork15':
            for i in range(0,len(self.components)):
                cmptype = self.components[i]['cmptype']
        elif self.importedfiletype == 'rkt':
            pass
            