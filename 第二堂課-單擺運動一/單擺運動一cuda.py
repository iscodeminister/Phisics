from vpython import *
import math
import os
os.environ['CUDA_VISIBLE_DEVICES']='0'
def main():
    scene = canvas(title="單擺運動一", width=1600, height=900, x=0, y=0)
    ceiling = box(pos=vec(0, 0, 0),length=2,height=0.02,width=2,opacity=0.5)
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
    #@vectorize(["float32(float32, float32, float32)"], target='cuda')
    def calcA(r,v,t):
        axis = r - ceiling.pos
        uaxis = axis.norm()
        ac = mag2(v)/mag(axis)
        at = g-g.dot(uaxis)*uaxis
        return at-ac*uaxis
    rmass = 0.01
    angle=20
    theta= radians(angle)

    rod.mass = rmass
    rod.theta0 = theta + pi*3/2
    rod.L0 = 1
    bob.mass = 0.2
    bob.pos=ceiling.pos + vector(
        rod.L0*cos(rod.theta0),
        rod.L0*sin(rod.theta0),
        0
    )
    bob.v = vector(0,0,0)
    bob.a = calcA(
        bob.pos,bob.v,0
    )
    scene.center =  vector(0,-rod.L0,0)
    rod.axis = bob.pos-ceiling.pos



    t = 0
    dt = 0.00001
    while t <50:
        rate(10000)
        bob.pos += bob.v*dt
        bob.v+=bob.a*dt
        bob.a = calcA(
        bob.pos,bob.v,0
        )
    
        rod.axis = bob.pos - ceiling.pos
        t += dt
    return
main()