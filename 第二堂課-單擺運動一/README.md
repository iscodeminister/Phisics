# 第二堂課-單擺運動一
## Task lists
- [ ] 矩形法（等速度運動公式，r⃗=r⃗+v⃗ dt）可以採用【左】矩形，也可以採用【右】矩形來計算，比較一下兩種做法的誤差。
- [x] 比較矩形法和梯形法（等加速度運動公式，r⃗=r⃗+v⃗ dt+(1/2) a⃗ dt^2）的誤差
## 報告
### 1.單擺運動一 歐拉法
  - 要做到什麼事？<br>
      使用`python`的外掛`vpython`來模擬繪製與計算物理實驗內容<br>
      使用程式計算手算困難的單擺運動<br>
      測試*不同積分方法*會不會明顯影響實驗結果<br><br>
  - 如何做到那件事？<br>
      用vpython繪製一個大平面(天花板)，一條擺繩，跟一個擺錘<br>
      給定兩球的角度、重量、半徑以及重力常數後作運算[程式碼](/第二堂課-單擺運動一/單擺運動一.py)<br>
      ```
      rod = cylinder( #擺繩
      axis=vector(0,-1,0),
      radius=0.0005,
      opacity=0.5
      )
      bob = sphere( #擺錘
      radius = 0.025,
      make_trail = True,
      opacity = 0.5
      )
      ``` 
      運算完之後確認實驗數據<br><br>
  - 做出來的結果<br>
      ![This is an image](/第二堂課-單擺運動一/result1.png)<br>
      <br>
      上圖是使用矩形法做積分得到的結果，而下圖是使用梯形法做積分得到的結果<br>
      <br>
      ![This is an image](/第二堂課-單擺運動一/result2.png)<br>
      <br>
      看起來梯形法似乎有比較精準一點，但不大明顯，我把dt改成0.001試試<br><br>
      ![This is an image](/第二堂課-單擺運動一/result1dt.png)<br>
      ![This is an image](/第二堂課-單擺運動一/result2dt.png)<br><br>
      差異還是看不大出來，我將dt調整為0.00005並加上刻度觀察90度處<br><br>
      ![This is an image](/第二堂課-單擺運動一/result1pdtc.png)<br>
      ![This is an image](/第二堂課-單擺運動一/result2pdtc.png)<br>
      終於看出來了，下圖(梯形法)能取得較高精準度(約精準40%)<br>
  - 結論<br>
      經過python的作圖分析結果，得知`當使用歐拉法時`**梯形法比矩形法更佳精確**