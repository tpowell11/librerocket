from tkinter import *

def drawTube(canvas: Canvas ,length: float, diameter: float):
    "Draws a bodytube to a tk canvas"
    width, height = int(canvas.cget('width')), int(canvas.cget('height'))
    canvas.create_rectangle((height/2)+10, (height/2)-10, (width/2)+100, (width/2)-100, width=5, fill='red')
def drawEllipticCone(canvas: Canvas, length: float, baseod: float):
    "Draws an elliptic nosecone to a tk canvas"
    
def drawConicalCone(canvas: Canvas, length: float, baseod: float):
    "Draws an conical nosecone to a tk convas"

def drawOgiveCone(canvas: Canvas, length: float, baseod: float):
    "Draws an ogive nosecone to the canvas"