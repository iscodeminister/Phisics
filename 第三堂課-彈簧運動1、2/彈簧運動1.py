from vpython import *
import math

"scene"

#scene = canvas(title="彈簧運動一", width=1600, height=900)
floor = box(width=1, height=0.02, length=2, opacity=0.5)
spring = helix(pos=floor.pos,
    axis=vector(floor.length/4,0,0),
	radius=0.03, coils=20
)
ball = sphere(
    pos=spring.pos+spring.axis,
	radius=0.1, make_trail=False, interval=30
)
g = vector(0,-9.8,0)

def calcA(r,v,t):
    return (-spring.k*(r-spring.r0))/ball.mass

spring.L0 = spring.axis.mag
spring.k = 50

ball.mass = 0.5
ball.mg = ball.mass*9.8

ball.pos.y += ball.radius+floor.height/2
spring.pos.y = ball.pos.y
spring.r0 = spring.pos+spring.axis

ball.pos.x += spring.L0/2
ball.v = vector(0,0,0)
ball.a = calcA(ball.pos,ball.v,0)
ball.make_trail = True

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

"graph"
x_t = gcurve(label='x 位置 x10',color=color.red)
v_t = gcurve(label='x 速度',color=color.green)
a_t = gcurve(label='x 加速度',color=color.blue)

"count"
dt = 0.0001
t = 0
while t<3:
    rate(2000)
    ball.pos,ball.v,ball.a = nextValue(
        ball.pos,ball.v,calcA,t,dt,ball.a
    )
    spring.axis = ball.pos-spring.pos

    x_t.plot(t,ball.pos.x*10)
    v_t.plot(t,ball.v.x)
    a_t.plot(t,ball.a.x)
    
    t += dt