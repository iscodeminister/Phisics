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
mass = 0.280
v0 = 15
radius = 0.105

g = vector(0,-9.8,0)

csvFile = open('out1to89.csv','w',newline='') #csv
Writer = csv.writer(csvFile)
Writer.writerow(['angle','Distance'])

"""
def
"""
bally = radius + floor.height/2


"""
計算迴圈
"""
for bangle in range(1,90):
	the= radians(bangle)
	ball_b = sphere(radius=radius,make_trail=True,pos=vector(end,bally,0),interval=10,color=color.white) #考慮空氣阻力的球
	if bangle==45:
		ball_b.color=color.green
	#scene.camera.follow(ball_b)

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
	dt = 0.0001
	while True:
		rate(4000)
		if ball_b.pos.y < ball_b.y0:
			break

		if ball_b.pos.y >= ball_b.y0:
			ball_b.pos += ball_b.v*dt
			ball_b.a = g + (1.225*-0.5*ball_b.v.mag2*0.5*pi*ball_b.radius**2*ball_b.v.norm())/ball_b.m
			ball_b.v += ball_b.a*dt
	ball_b.make_trail = False
	dist= ball_b.pos.x-end
	print("球以角度",bangle,"飛了",dist,"公尺",sep='')
	Writer.writerow([bangle,dist])

csvFile.close()