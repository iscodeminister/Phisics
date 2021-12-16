from vpython import *
import math

"""
設計場景
"""
scene.range=1.2                             # 設定攝影機範圍在正負 1.2 公尺
scene.g = vector(0,-9.8,0)                  # 重力加速度

ceiling = box(                              # 產生一個扁平盒子代表天花板，取名為 ceiling（就是天花板）
    width=2,                                # 寬度（z-方向）為 2 公尺
	height=0.022,                           # 高度（y-方向）為 0.022 公尺（2.2 公分）
	length=2,                               # 長度（x-方向）為 2 公尺
	opacity=0.3                             # 【不】透明度為 0.3（頗透明）
)

rod = cylinder(                             # 產生一個細圓柱代表擺繩，取名為 rod（桿）
	axis=vector(0,-1,0),                    # 指向 -y 方向（下方）
	radius=0.0005,                          # 半徑為 0.0005 公尺（0.5 公厘）
	opacity=0.5                             # 【不】透明度為 0.5（半透明）
)

bob = sphere(                               # 產生一個球代表擺錘，取名為 bob（就是擺錘）
	radius=0.025,                           # 半徑為 0.025 公尺（2.5 公分）
	make_trail=True,                        # 要留下軌跡
	opacity=0.5                             # 【不】透明度為 0.5
)
def calcA(r,v,t):
    axis = r - ceiling.pos
    uaxis = axis.norm()
    ac = mag2(v)/mag(axis)
    at = scene.g-scene.g.dot(uaxis)*uaxis
    return at-ac*uaxis
def conicalSpeed(L,A):
    return sqrt(L*9.8*sin(A)*tan(A))
rmass = 0.01
angle=20
theta= radians(angle)

"""
def
"""
rod.mass = 0.01                             # 擺繩質量
rod.L0 = 1                                  # 擺繩原長
rod.theta0 = 20.0*pi/180.0                  # 初始 theta 角（從 -z 軸量起），可隨意更改看效果
rod.phi0 = 0.0*pi/180.0                     # 初始 phi 角（經度），可隨意更改看效果

bob.pos=ceiling.pos+vector(                 # 設定擺錘初始位置
    rod.L0*sin(pi-rod.theta0)*cos(rod.phi0),# 根據擺繩的初始角度來計算
    rod.L0*sin(pi-rod.theta0)*sin(rod.phi0),# 由於單擺的 theta 角定義是從 -z 軸量起的，但這裡我們用的是球座標
    cos(pi-rod.theta0)						# 公式來計算位置，角度得從 +z 軸量起，所以要換算成 pi-theta
)
bob.mass = 0.2                              # 擺錘質量 0.15 kg (150 g)

rod.axis = bob.pos-ceiling.pos              # 調整擺繩讓它連結擺錘與天花板
bob.velocity = conicalSpeed(                # 圓錐擺的速率
    rod.L0,rod.theta0
)*3*rod.axis.cross(scene.g).norm()          # 沿著 y-方向

bob.acceleration = calcA(                   # 初始加速度
    bob.pos,bob.velocity,0
)

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
dt = 0.001                                  # 時間間隔
while t < 50:
    rate(1000)                              # 每秒最多畫面數，慢一點方便觀察
    
    bob.pos,bob.velocity,bob.acceleration = nextValue(
        bob.pos,bob.velocity,calcA,t,dt
    )
    
    #scene.center = bob.pos                 # 攝影機聚焦在擺錘（可以極近距離觀察）
    rod.axis = bob.pos - ceiling.pos        # 更新擺繩
    t += dt                                 # 紀錄時間