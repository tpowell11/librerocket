#classes for LibreRocket
class component(object):
    "Basic fields for all components"
    mass: float
    diameter: float
class motor(component):
    "Fields for motors"
    def __init__(self, Itot: float, Diameter: float, Mass: float, Length: float, Curve: dict):
        #Moves data into the correct areas
        self.Itot = Itot
        self.diameter = Diameter
        self.mass = Mass
        self.length = Length
        self.curve = Curve