from vpython import *
import csv

"""
設計場景
"""
L=30 #箱子長度
scene = canvas(title="拋體運動三", width=1600, height=900, x=0, y=0)
floor = box(pos=vec(0, 0, 0),length=L, height=0.01, width=8,opacity=0.5)
end = -L/2
arrow(axis=vector(1,0,0),color=vector(1, 0, 0),shaftwidth=0.02,opacity=0.4,pos=vec(end,0,0))
arrow(axis=vector(0,1,0),color=vector(0, 1, 0),shaftwidth=0.02,opacity=0.4,pos=vec(end,0,0))
arrow(axis=vector(0,0,1),color=vector(0, 0, 1),shaftwidth=0.02,opacity=0.4,pos=vec(end,0,0))
mass = 0.0567 #weight
v0 = 60 #start speed
radius = 0.06858/2
bangle=45
theta= radians(bangle)
g = vector(0,-9.8,0)

csvFile = open('out.csv','w',newline='') #csv
Writer = csv.writer(csvFile)
Writer.writerow(['Ball','Distance'])

"""
def
"""
bally = radius + floor.height/2
ball_a = sphere(radius=radius,make_trail=True,
                pos=vector(end,bally,0),
                interval=10,color=color.green,
                opacity=0.4) #不考慮空氣阻力的透明球
ball_b = sphere(radius=radius,make_trail=True,
                pos=vector(end,bally,0.2),
                interval=10,color=color.yellow) #考慮空氣阻力的球
scene.camera.follow(ball_b) #Camera follow ball b
#ball a
#ball_a.pos.y = ball_a.radius+floor.height/2
ball_a.theta = theta
ball_a.y0 = ball_a.pos.y
ball_a.m = mass
ball_a.v0 = v0
ball_a.v = vector(
	ball_a.v0*cos(ball_a.theta),
	ball_a.v0*sin(ball_a.theta),
	0
)
ball_a.a = g

#ball b
#ball_b.pos.y = ball_b.radius+floor.height/2
ball_b.theta = theta
ball_b.y0 = ball_b.pos.y
ball_b.m = mass
ball_b.v0 = v0
ball_b.v = vector(
	ball_b.v0*cos(ball_b.theta),
	ball_b.v0*sin(ball_b.theta),
	0
)
ball_b.a = g