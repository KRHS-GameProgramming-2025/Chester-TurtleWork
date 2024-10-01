from shapes_new import *

def house (t, size = 10, color=None):
        square(t, size*5, 0, None, color)
        
        move(t, size*0, size*3)
        move(t, size*1, size*0)
        window(t, size)
        move(t, size*0, size*-3)
        move(t, size*-1, size*0)
        
        move(t, size*-1, size*5)
        roof(t, size, "black")
        move(t, size*1, size*-5)

        move(t, size*2.2, 0)
        door(t, size, "red")
        move(t, size*-2.2, 0)

def door(t, size =10, color=None):
    rect(t, size*.8, size*1.5, 0, None, color)
    
    move(t, size*.2, size*.9)
    window(t, size*.4)
    move(t, size*-.2, size*-.9)
    
    move(t, size*.7, size*.7)
    arc(t, size*.06, 360, 0, None, "black")
    move(t, size*-.7, size*-.7)

def roof(t, size =3, color=None):
    chim(t,size,size)
    
    sss_tri(t, size*7, size*4.5, size*4.5, 0, None, color)
    
    move(t, size*3, size*1)
    window(t, size)
    move(t, size*-3, size*-1)
    
    
def window(t,size =10):
    square(t, size*1, 0, None, "white")
    move(t, size*.5, size*0)
    line(t, size*0, size*1)
    move(t, size*.5, size*-.5)
    line(t, size*-1, size*0)
    move(t, size*0, size*-.5)
    
    
    
def chim(t, size=5, color=None):
    move(t, size*5, size*.8)
    rect(t, size*.5, size*1.5, 0, None, "yellow")
    move(t, size*-5, size*-.8)
