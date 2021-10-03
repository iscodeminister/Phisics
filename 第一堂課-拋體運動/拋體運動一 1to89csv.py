from os import read
from vpython import *
import csv

"""
設計場景
"""
L=15 #箱子長度
bangles=[15,30,45,60,75]
scene = canvas(title="拋體運動", width=800, height=400, x=0, y=0)
floor = box(pos=vec(0,0,0),length=L, height=0.02, width=10)

csvFile = open('out2.csv','w',newline='') #csv
Writer = csv.writer(csvFile)
Writer.writerow(['Angle','Distance'])

"""
計算迴圈
"""
for bangle in range(1,90):
	ball = sphere(radius=0.05,make_trail=True,color=color.red)
	ball.pos.x = -floor.length/2
	ball.pos.y = ball.radius+floor.height/2
	ball.y0 = ball.pos.y
	ball.m = 0.1 
	ball.v0 = 10
	bangle1=bangle    
	the= radians(bangle1)
	ball.theta = the

	ball.v = vector(          
		ball.v0*cos(ball.theta),
		ball.v0*sin(ball.theta),
		0
	)

	ball.a = vector(0,-9.8,0)         


	dt = 0.0001

	while ball.pos.y >= ball.y0: 	

		ball.pos = ball.pos+ball.v*dt	
		ball.v = ball.v+ball.a*dt		
		rate(100000)

	bdist=ball.pos.x + L/2
	print("在拋射角為",bangle,"度時,球飛了",bdist,"公尺",sep='')
	Writer.writerow([bangle,bdist])
	ball = sphere(radius=0.05,make_trail=False,color=color.red)


csvFile.close()