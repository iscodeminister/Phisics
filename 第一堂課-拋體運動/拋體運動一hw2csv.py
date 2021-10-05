from os import read
from vpython import *
import csv

"""
設計場景 假設人高180
"""
L=15 #箱子長度
bangles=[15,30,45,60,75]
scene = canvas(title="拋體運動2", width=800, height=400, x=0, y=0)
floor = box(pos=vec(0,0,0),length=L, height=0.02, width=10)
bx=-floor.length/2
by=floor.height/2+0.9
man = box(pos=vector(bx,by,0),length=0.5, height=1.8, width=1)

csvFile = open('out3.csv','w',newline='') #csv
Writer = csv.writer(csvFile)
Writer.writerow(['Angle','Distance'])

"""
計算迴圈
"""
for bangle in bangles:
	ran=bangle/15 #判斷角度
	if ran==1:
		ball = sphere(radius=0.05,make_trail=True,color=color.red)
	elif ran==2:
		ball = sphere(radius=0.05,make_trail=True,color=color.green)
	elif ran==3:
		ball = sphere(radius=0.05,make_trail=True,color=color.purple)
	elif ran==4:
		ball = sphere(radius=0.05,make_trail=True,color=color.blue)
	elif ran==5:
		ball = sphere(radius=0.05,make_trail=True,color=color.white)
	ball.pos.x = -floor.length/2
	ball.pos.y = ball.radius+floor.height/2+1.8
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

	while ball.pos.y >= ball.y0-1.8: 	

		ball.pos = ball.pos+ball.v*dt	
		ball.v = ball.v+ball.a*dt		
		rate(1000)

	bdist=ball.pos.x + L/2
	print("在拋射角為",bangle,"度時,球飛了",bdist,"公尺",sep='')
	Writer.writerow([bangle,bdist])
	ball = sphere(radius=0.05,make_trail=False,color=color.red)


csvFile.close()