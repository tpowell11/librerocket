import os
import json

def getFileAsList(file: str):
    "return the ui elements of a rocket file"
    with open(file, "r") as f:
        return json.