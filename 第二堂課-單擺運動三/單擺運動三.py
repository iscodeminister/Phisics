from vpython import *
import math

"""
設計場景
"""
scene = canvas(title="單擺運動三", width=1600, height=900, x=0, y=0)
ceiling = box(pos=vec(0, 0, 0),length=2,
    height=0.02,width=2,opacity=0.5)
arrow(axis=vector(0,-1.5,0),color=vector(0, 1, 0),shaftwidth=0.01,opacity=0.4)
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
def calcA(r,v,t):
    axis = r - ceiling.pos
    uaxis = axis.norm()
    ac = mag2(v)/mag(axis)
    at = g-g.dot(uaxis)*uaxis
    return at-ac*uaxis
def conicalSpeed(L,A):
    return sqrt(L*9.8*sin(A)*tan(A))
rmass = 0.01
angle=20
theta= radians(angle)

"""
def
"""
rod.mass = rmass
rod.theta0 = theta
rod.phi0 = radians(0)
rod.L0 = 1
bob.mass = 0.2
bob.pos=ceiling.pos + vector(
    rod.L0*sin(pi-rod.theta0)*cos(rod.phi0),
    rod.L0*sin(pi-rod.theta0)*sin(rod.phi0),
    cos(pi-rod.theta0)
)
bob.v = conicalSpeed(rod.L0,rod.theta0)*3*rod.axis.cross(g).norm()
bob.a = calcA(
    bob.pos,bob.v,0
)
#scene.center =  vector(0,-rod.L0,0)
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
    rate(1000)
    bob.pos,bob.v,bob.a = nextValue(bob.pos,bob.v,calcA,t,dt)
    #if t>49.95:
    #    if bob.pos.x == 0:
    #        print("t值為",t,"y值為",bob.pos.y,sep='')
    rod.axis = bob.pos - ceiling.pos
    t += dt