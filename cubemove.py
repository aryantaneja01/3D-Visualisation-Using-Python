from visual import *
from visual.controls import *
def setdir(direction):
    cube.dir=direction
def togglecubecolor():
    if(t1.value):
        cube.color=color.cyan
    else:
        cube.color=color.red
def cubecolor(value):
    cube.color=value
    if(cube.color==color.red):
        t1.value=0
    else:
        t1.value=1
def setrate(obj):
    cuberate(obj.value)
    if(obj is s1):
        s2.value=s1.value
    else:
        s1.value=s2.value
def cuberate(value):
    cube.dtheta=2*value*pi/1e4
w=350
display(x=w,y=0,width=w,range=1.5,forward=-vector(0,1,1))
cube=box(color=color.red)
c=controls(x=0,y=0,width=w,height=w,range=60)
bl=button(pos=(-30,30),height=30,width=40,text='Anti-clk',action=lambda:setdir(-1))
br=button(pos=(30,30),height=30,width=40,text='clk',action=lambda:setdir(1))
s1=slider(pos=(-15,-40),width=7,length=70,axis=(1,0.7,0),action=lambda:setrate(s1))
s2=slider(pos=(-15,-40),width=7,length=50,axis=(0,1,0),action=lambda:setrate(s2))
t1=toggle(pos=(40,-30),width=10,height=10,text0="Red",text1="Cyan",action=lambda:togglecubecolor())
m1=menu(pos=(0,0,0),height=7,width=25,text='Options')
m1.items.append(('Anti-clk',lambda:setdir(-1)))
m1.items.append(('Clk',lambda:setdir(1)))
m1.items.append(('______',None))
m1.items.append(('Red',lambda:cubecolor(color.red)))
m1.items.append(('Cyan',lambda:cubecolor(color.cyan)))
s1.value=70
setrate(s1)
setdir(-1)
while(True):
    rate(100)
    cube.rotate(axis=(0,1,0),angle=cube.dir*cube.dtheta)

    

        
    
