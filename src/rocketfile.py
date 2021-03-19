from lxml import etree
import zipfile
import pprint
def getlistfromork(filepath:str)->list:
    pp=pprint.PrettyPrinter(indent=4)
    zf = zipfile.ZipFile(filepath,mode='r') #declare the actual file binary
    f = zf.open('rocket.ork') #open the internal file from the zip
    m=[]
    has_attributes = ['innertube','bulkhead','tubecoupler','masscomponent','nosecone','parachute','bodytube',
    'shockcord','freeformfinset','centeringring','motormount']
    #these lists define where specific elements are processed
    is_value_string=['finish','shape','masscomponenttype','designation','cd','deployevent','deployaltitude']
    is_value_float=['length','thickness','aftradius','aftshoulderlength','aftshoulderthickness','mass',
                    'packedlength','packedradius','radialposition','radialdirection','radius','outerradius',
                    'diameter','delay','linelength','linecount','deploydelay','fincount','rotation','cant','tabheight'
                    'tablength','filletradius']
    is_value_bool=['aftshouldercapped']
    is_material=['material','linematerial','filletmaterial']
    root=etree.parse(f)

    for element in root.iter('*'): #get all of the tags in the document
        if element.tag in has_attributes:
            m.append([element.tag]) #append the part's name to the list
        #general processing for elements whose data is stored in element text
        try:
            if element.tag in is_value_float:
                m[-1].append([element.tag,float(element.text)])
            if element.tag in is_value_string: #make the element's payload a float
                m[-1].append([element.tag,str(element.text)])
            if element.tag in is_value_bool: #make the element's payload a bool
                m[-1].append([element.tag,bool(element.text)])
        except ValueError:
            m[-1].append([element.tag,element.text])
        #special processing for elements that use XML attibutes or do not work with the above
        if element.tag == 'preset':
            m[-1].append([element.tag,element.get('manufacturer'),element.get('partno'),element.get('digest')])
        if element.tag == 'position':
            m[-1].append([element.tag,float(element.text),element.get('type')])
        if element.tag == 'motor':
            m[-1].append([element.tag,element.get('configid')])
        if element.tag == 'tabposition':
            m[-1].append([element.tag,float(element.text),element.get('relativeto')])
        if element.tag in is_material:
            m[-1].append([element.tag,element.text,element.get('type'),float(element.get('density'))])
        if element.tag == 'finpoints':
            m[-1].append([element.tag]) #finpoints are a group of attributes to the fins and need to be processed as such
        if element.tag == 'point':
            m[-1][-1].append([element.tag,element.get('x'),element.get('y')]) #group finpoints with their parent
    pp.pprint(m)
getlistfromork('hell.ork')
