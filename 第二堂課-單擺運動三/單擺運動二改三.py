from vpython import *
import math

"""
設計場景
"""
scene = canvas(title="單擺運動二to三", width=1600, height=900, x=0, y=0)
ceiling = box(pos=vec(0, 0, 0),length=2,
    height=0.02,width=2,opacity=0.5)
arrow(axis=vector(0,-1.5,0),color=vector(0, 1, 0),shaftwidth=0.01,opacity=0.4)
count = 0
while count<150:
    y = count/100
    box(pos=vector(0,-y,0),axis=vector(0,0.0001,0),color=color.red,height=0.02, width=0.001)
    count+=1
g = vector(0,-9.8,0)
rod = cylinder(
    axis=vector(0,-1,0),
    radius=0.0005,
    opacity=0.5
)
bob = sphere(
    radius = 0.025,
    make_trail = True,
    opacity = 0.5
)
def conicalSpeed(L,A):
    return sqrt(L*9.8*sin(A)*tan(A))
def calcA(r,v,t):
    axis = r - ceiling.pos
    uaxis = axis.norm()
    ac = mag2(v)/mag(axis)
    at = g-g.dot(uaxis)*uaxis
    return at-ac*uaxis
rmass = 0.01
angle=20
theta= radians(angle)

"""
def
"""
rod.mass = rmass
rod.theta0 = theta + pi*3/2
rod.L0 = 1
bob.mass = 0.2
bob.pos=ceiling.pos + vector(
    rod.L0*cos(rod.theta0),
    rod.L0*sin(rod.theta0),
    0
)
bob.v = vector(0,0,conicalSpeed(rod.L0,theta))
bob.a = calcA(
    bob.pos,bob.v,0
)
scene.center =  vector(0,-rod.L0,0)
rod.axis = bob.pos-ceiling.pos
"""
Runge-Kutta
"""
def nextValue(r,v,A,t,dt,a_now = None):
    r1 = r
    v1 = v
    a1 = a_now
    if a1 is None: a1 = A(r1,v1,t)
    
    dt2 = dt*0.5
    r2 = r+dt2*v1
    v2 = v+dt2*a1
    a2 = A(r2,v2,t+dt2)
    
    r3 = r+dt2*v2
    v3 = v+dt2*a2
    a3 = A(r3,v3,t+dt2)
    
    r4 = r+dt*v3
    v4 = v+dt*a3
    a4 = A(r4,v4,t+dt)
    
    dt /= 6.0
    r += (v1+(v2+v3)*2.0+v4)*dt
    v += (a1+(a2+a3)*2.0+a4)*dt
    
    return (r,v,A(r,v,t+dt))

"""
Compute
"""
t = 0
dt = 0.0005
while t <50:
    rate(2000)
    bob.pos,bob.v,bob.a = nextValue(bob.pos,bob.v,calcA,t,dt)
    rod.axis = bob.pos - ceiling.pos
    if t==49:
        print(mag(bob.pos))
    t += dt