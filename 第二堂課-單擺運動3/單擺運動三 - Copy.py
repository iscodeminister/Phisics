from vpython import *
import math

GlowScript 3.2 VPython

"""
設計場景
"""
scene = canvas(title="單擺運動三", width=1600, height=900)
ceiling = box(pos=vec(0, 0, 0),length=2,
    height=0.02,width=2,opacity=0.5)
#arrow(axis=vector(0,-1.5,0),color=vector(0, 1, 0),shaftwidth=0.01,opacity=0.4)
scene.g = vector(0,-9.8,0)
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
    at = scene.g-scene.g.dot(uaxis)*uaxis
    return at-ac*uaxis

angle=20.0
theta= radians(angle)

"""
def
"""
v0=2
rod.mass = 0.01
rod.theta0 = theta
rod.phi0 = radians(0.0)
rod.L0 = 1.0
bob.mass = 0.2
bob.pos=ceiling.pos + vector(
    rod.L0*sin(pi-rod.theta0)*cos(rod.phi0),
    rod.L0*sin(pi-rod.theta0)*sin(rod.phi0),
    cos(pi-rod.theta0)
)
rod.axis = bob.pos-ceiling.pos
#bob.v = vector(0,0,1.1045155)
bob.v = conicalSpeed(rod.L0,rod.theta0-3/2*pi)*v0*rod.axis.cross(scene.g).norm()
bob.a = calcA(bob.pos,bob.v,0)
#scene.center =  vector(0,-rod.L0,0)

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
    rate(1000)
    bob.pos,bob.v,bob.a = nextValue(bob.pos,bob.v,calcA,t,dt)
    #if t>49.95:
    #    if bob.pos.x == 0:
    #        print("t值為",t,"y值為",bob.pos.y,sep='')
    #print(bob.pos.y)
    rod.axis = bob.pos - ceiling.pos
    t += dt