# NAME: 

from turtle import *
from math import *


def equilateral_tri(t, size=100, rotate=0, lineColor=None, fillColor=None):
    print ("Equilateral Triangle, with Size:", size, "and Rotation:", rotate)
    if lineColor!=None:
        lc=t.pencolor()
        t.pencolor(lineColor)
    if fillColor!=None:
        fc=t.fillcolor()
        t.fillcolor(fillColor)
        t.begin_fill()
    t.lt(rotate)
    count = 0
    while count < 3:
        t.fd(size)
        t.lt(120)
        count += 1
    t.rt(rotate)
    if fillColor!=None:
        t.end_fill()
        t.fillcolor(fc)
    if lineColor!=None:
        t.pencolor(lc)

#--------------------------QUADRILATERALS-------------------------#

def para(t, width=100, height=100, big_angle=120, rotate=0, lineColor=None, fillColor=None):
    print ("Parallelogram, with Width:", width, "Height:", height, "Large Angle:", big_angle, "and Rotation:", rotate)
    if lineColor!=None:
        lc=t.pencolor()
        t.pencolor(lineColor)
    if fillColor!=None:
        fc=t.fillcolor()
        t.fillcolor(fillColor)
        t.begin_fill()
    t.lt(rotate)
    count = 0
    while count < 4:
        t.fd(height)
        t.lt(big_angle)
        t.fd(width)
        t.lt(180-big_angle)
        count += 2
    t.rt(rotate)
    if fillColor!=None:
        t.end_fill()
        t.fillcolor(fc)
    if lineColor!=None:
        t.pencolor(lc)

def rhom(t, size=100, big_angle=120, rotate=0, lineColor=None, fillColor=None):
    print ("Rhombus, with Size:", size, "Large Angle:", big_angle, "and Rotation:", rotate)
    para(t,size,big_angle,rotate,180-big_angle,lineColor,fillColor)
  
def rect(t, width=100, height=100, rotate=0, lineColor=None, fillColor=None):
    print ("Rectangle, with Width:", width, "Height:", height, "and Rotation:", rotate)
    para(t,width,height,90,rotate,lineColor,fillColor)

def square(t, size=100, rotate=0, lineColor=None, fillColor=None):
    print ("Sqaure, with Size:", size, "and Rotation:", rotate)
    para(t,size,size,90,rotate,lineColor,fillColor)
    
  
#-------------------------------POLYGONS--------------------------#

def poly(t, sides=5, size=100, rotate=0, lineColor=None, fillColor=None):
    print ("Polygon, with Sides:", sides, "Size:", size, "and Rotation:", rotate)
    if lineColor!=None:
        lc=t.pencolor()
        t.pencolor(lineColor)
    if fillColor!=None:
        fc=t.fillcolor()
        t.fillcolor(fillColor)
        t.begin_fill()
    t.lt(rotate)
    count = 0
    while count < 5:
        t.fd(size)
        t.lt(72)
        count += 1
    t.rt(rotate)
    if fillColor!=None:
        t.end_fill()
        t.fillcolor(fc)
    if lineColor!=None:
        t.pencolor(lc)

def star(t, points=5, size=100.0, rotate=0, lineColor=None, fillColor=None):
    print ("Star, with Points:", points, "Size:", size, "and Rotation:", rotate)
    if lineColor!=None:
        lc=t.pencolor()
        t.pencolor(lineColor)
    if fillColor!=None:
        fc=t.fillcolor()
        t.fillcolor(fillColor)
        t.begin_fill()
    t.lt(rotate)
    count = 0
    while count < points:
        t.fd(size)
        t.lt(180-(180-2*(360/points)))
        count += 1
    t.rt(rotate)
    if fillColor!=None:
        t.end_fill()
        t.fillcolor(fc)
    if lineColor!=None:
        t.pencolor(lc)


#------------------------------MOVEMENT---------------------------#

def line(t, x=100, y=100, lineColor=None):
    print ("Line to a point X:", x, "over and Y:", y, "up")
    if lineColor!=None:
        lc=t.pencolor()
        t.pencolor(lineColor)
    dist=sqrt(x**2+y**2)
    angle=degrees(atan(y/x))
    t.lt(angle)
    t.fd(dist)
    t.rt(angle)
    if lineColor!=None:
        t.pencolor(lc)

  
def move(t, x, y):
    print ("Move without marking a line to a point X:", x, "over and Y:", y, "up")
    t.pu()
    line(t,x,y)
    t.pd()


