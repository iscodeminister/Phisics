# 第三堂課-單擺運動一、二
## Task lists
- [x] 繪製出【位置 vs 時間】以及【能量 vs 時間】的數據圖。
## 報告
### 1.彈簧運動－經典範例與能量守恆
  - 要做到什麼事？<br>
      使用`python`的外掛`vpython`來模擬繪製與計算物理實驗內容<br>
      使用程式計算手算困難的簡諧運動<br>
      並使用vpython的繪圖功能繪製圖表<br><br>
  - 如何做到那件事？<br>
      用vpython繪製一個大平面(地板)，一條彈簧，跟一個球體<br>
      給定彈簧及球的半徑以及重力常數與榮格-庫塔方法後作運算[程式碼](/第三堂課-彈簧運動1、2/彈簧運動集合.py)<br>
      ```
      spring = helix(pos=floor.pos,
      axis=vector(floor.length/4,0,0),
	  radius=0.03, coils=20
      )
      ball = sphere(
      pos=spring.pos+spring.axis,
	  radius=0.1, make_trail=False, interval=30
      )
      ``` 
      運算完之後確認實驗數據<br><br>
  - 做出來的結果<br><br>
      ![This is an image](/第三堂課-彈簧運動1、2/preview.png)<br>
      <br>
      上圖是做出來得到的結果<br>
      但我們看不到任何數據跟關係<br>
      所以要製作數據圖<br><br>
      ![This is an image](/第三堂課-彈簧運動1、2/xtplot.png)<br>
      ![This is an image](/第三堂課-彈簧運動1、2/keue.png)<br>
      ![This is an image](/第三堂課-彈簧運動1、2/et.png)<br>
      <br>
      看起來榮格-庫塔法幾乎沒有誤差，取位置的絕對值恆為1<br>
  - 結論<br>
      經過python的作圖分析結果，得知`榮格-庫塔方法`**能以簡單計算獲得能接受的結果**
