from os import read
from vpython import *
import csv

"""
設計場景
"""
L=15
bangles=[15,30,45,60,75]
scene = canvas(title="拋體運動", width=800, height=400, x=0, y=0)
floor = box(length=L, height=0.02, width=10)
# 圓球是我們要拋出的物體，半徑 0.05 米（5 公分），並且留下軌跡（make_trail=True）
#ball = sphere(radius=0.05,make_trail=True,color=color.red)

csvFile = open('out.csv','w',newline='') #csv
Writer = csv.writer(csvFile)
Writer.writerow(['Angle','Distance'])

"""
初始條件
"""
for bangle in bangles:
	ran=bangle/15
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

	while ball.pos.y >= ball.y0: 		# 迴圈開始，當球的高度（y 座標）還大於初始高度（表示球還在空中），執行下列計算

		ball.pos = ball.pos+ball.v*dt	# 用現在的速度計算下一個時間點的位置，並更新球的位置
		ball.v = ball.v+ball.a*dt		# 用現在的加速度計算下一個時間點的速度
		rate(1000)

	bdist=ball.pos.x + L/2
	print("在拋射角為",bangle,"度時,球飛了",bdist,"公尺",sep='')
	Writer.writerow([bangle,bdist])
	ball = sphere(radius=0.05,make_trail=False,color=color.red)





csvFile.close()
