
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
