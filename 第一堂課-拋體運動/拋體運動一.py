from vpython import *

"""
設計場景
"""
L=15
bangle=45
scene = canvas(title="Projection", width=800, height=400, x=0, y=0)
floor = box(length=L, height=0.02, width=10)
# 圓球是我們要拋出的物體，半徑 0.05 米（5 公分），並且留下軌跡（make_trail=True）
ball = sphere(radius=0.05,make_trail=True,color=color.red)
# 將圓球放到地板左側邊
ball.pos.x = -floor.length/2
# 再放到地板表面
ball.pos.y = ball.radius+floor.height/2
# 紀錄這個初始高度
ball.y0 = ball.pos.y

"""
初始條件
"""
ball.m = 0.1                 		# 球的質量為 0.1 公斤（100 公克）

ball.v0 = 10              			# 球的初速率為 10 m/s（相當於 36 km/hr）
the= radians(bangle)
ball.theta = the

ball.v = vector(                    # 計算初速度向量，把它取名為 ball.v
	ball.v0*cos(ball.theta),
	ball.v0*sin(ball.theta),
	0
)

ball.a = vector(0,-9.8,0)           # 球的加速度，忽略空氣阻力的話，受力只有重力，所以加速度只有重力加速度

'''
---------------------------------------------------------------------------------------------------------
細步計算
---------------------------------------------------------------------------------------------------------
'''

dt = 0.001							# 每次計算的時間間隔，千分之一 秒是模擬物理狀況時常見的設定
# 時間間隔越小，計算越準確，但計算時間就越長
while ball.pos.y >= ball.y0: 		# 迴圈開始，當球的高度（y 座標）還大於初始高度（表示球還在空中），執行下列計算

	ball.pos = ball.pos+ball.v*dt	# 用現在的速度計算下一個時間點的位置，並更新球的位置
	ball.v = ball.v+ball.a*dt		# 用現在的加速度計算下一個時間點的速度
	rate(1000)

print("在拋射角為",bangle,"度時,球飛了",ball.pos.x + L/2,"公尺",sep='')