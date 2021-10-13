from os import read
from vpython import *
import csv

"""
設計場景
"""
L=15 #箱子長度
scene = canvas(title="拋體運動\\(\\vec{f}\\)", width=800, height=400, x=0, y=0)
scene.caption = "\\( \\vec{f} \\)"
floor = box(pos=vec(0,0,0),length=L, height=0.01, width=8,opacity=0.5)
arrow(axis=vector(1,0,0),color=vector(1,0,0),shaftwidth=0.02,opacity=0.4)
arrow(axis=vector(0,1,0),color=vector(0,1,0),shaftwidth=0.02,opacity=0.4)
arrow(axis=vector(0,0,1),color=vector(0,0,1),shaftwidth=0.02,opacity=0.4)
mass = 0.0567
v0 = 5
radius = 0.06541
bangle=45
the= radians(bangle)
g = vector(0,-9.8,0) 

csvFile = open('out.csv','w',newline='') #csv
Writer = csv.writer(csvFile)
Writer.writerow(['Angle','Distance'])

"""
def
"""
bally = radius + floor.height/2
ball_a = sphere(radius=radius,make_trail=True,pos=vector(0,bally,0),interval=10,color=color.green,opacity=0.4) #不考慮空氣阻力的透明球
ball_b = sphere(radius=radius,make_trail=True,pos=vector(0,bally,0.2),interval=10,color=color.white) #考慮空氣阻力的球
scene.camera.follow(ball_a)
#ball a
#ball_a.pos.y = ball_a.radius+floor.height/2
ball_a.theta = the
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
ball_b.theta = the
ball_b.y0 = ball_b.pos.y
ball_b.m = mass
ball_b.v0 = v0
ball_b.v = vector(          
	ball_b.v0*cos(ball_b.theta),
	ball_b.v0*sin(ball_b.theta),
	0
)
ball_b.a = g 

"""
計算迴圈
"""
eta_air = 1.81e-5
b = 6*pi*eta_air*ball_b.radius	
dt = 0.0001
while True:
	rate(4000)
	if ball_a.pos.y >= ball_a.y0 and ball_b.pos.y < ball_b.y0:
	    break
	if ball_a.pos.y >= ball_a.y0:
		ball_a.pos += ball_a.v*dt
		ball_a.v += ball_a.a*dt

	if ball_b.pos.y >= ball_b.y0:
		ball_b.pos += ball_b.v*dt
		ball_b.a = g + (-b*ball_b.v/ball_b.m)
		ball_b.v += ball_b.a*dt



''''
bdist=ball.pos.x + L/2
print("在拋射角為",bangle,"度時,球飛了",bdist,"公尺",sep='')
Writer.writerow([bangle,bdist])
ball = sphere(radius=0.05,make_trail=False,color=color.red)


csvFile.close()
'''