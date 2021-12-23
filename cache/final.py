from vpython import *
import math

"""
 參數設定,資料來源
    太陽 https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html
    水星 https://nssdc.gsfc.nasa.gov/planetary/factsheet/mercuryfact.html
    金星 https://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html
    地球 https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
    火星 https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html
"""
#SI unit
radius = {"Sun": 695700000, "Mercury":2439700, "Venus": 6051800, "Earth": 6371000, }
mass = {"Sun": 1988500E24, "Mercury": 0.33010E24, "Venus": 4.8673E24, "Earth": 5.9722E24,}
material = {"Sun": color.orange, "Mercury": color.cyan, "Venus": color.yellow, "Earth": color.blue}
dist_apo = {"Mercury": 6982E7, "Venus": 10894E7, "Earth": 15210E7, "Mars": 24923E7}
v_apo = {"Mercury": 38860, "Venus": 34790, "Earth": 29290, "Mars": 21970}
G = 6.67408E-11       # 重力常數
t = 0                 # 時間
dt = 60*60            # 時間間隔

"""
 2. 產生行星類別 
"""
# 不用繼承的 class 寫法
class Planet:
    def __init__(self, pos, radius, mass, color):
        self.pos = pos
        self.radius = radius
        self.mass = mass
        self.color = color
        self.v = 0
        self.a = 0
        self.planet = sphere(pos = self.pos, radius = self.radius, mass = self.mass, \
                             color = self.color, make_trail = True, retain = 365)
    def update(self, dt):
        self.dt = dt
        self.a = -G*mass["Sun"] / self.planet.pos.mag2 * self.planet.pos.norm()
        self.v += self.a * self.dt
        self.planet.pos += self.v * self.dt

"""
 3. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 sphere 物件產生星球 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (3) 星球的半徑要手動調整比例, 否則會看不到星球
"""
scene = canvas(title = "Planetary Motion", width = 600, height = 600, x = 0, y = 0, background = color.black)
sun = sphere(pos = vector(0,0,0), radius = radius["Sun"]*20, color = color.orange, emissive = True)
# 原來的寫法為 scene.lights = [local_light(pos = vector(0,0,0), color = color.white)]
# 在 VPython 7 中 canvas.lights 無法設定為 local_light, 只能另外在太陽處放置另一個光源 lamp
lamp = local_light(pos = vector(0,0,0), color = color.white)
# 用 for 迴圈產生水星、金星、地球、火星
names = ["Mercury", "Venus", "Earth", "Mars"]
planets = []

for name in names:
    planets.append(Planet(pos = vector(d_at_aphelion[name], 0, 0), radius = radius[name]*2E3, mass = mass[name], \
                          color = material[name]))
    planets[-1].v = vector(0, v_at_aphelion[name], 0)

"""
 4. 星球運動部分
"""
while(True):
    rate(60*24)
# 用 for 迴圈自動跑完所有行星的資料
    for planet in planets:
        planet.update(dt)
# 更新時間
    t += dt