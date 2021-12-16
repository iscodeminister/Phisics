# 第二堂課-單擺運動二
## Task lists
- [x] 比較單擺運動一和單擺運動二的誤差。
## 報告
### 1.單擺運動二：夠實用的【四階 Runge-Kutta】方法
  - 要做到什麼事？<br>
      使用`python`的外掛`vpython`來模擬繪製與計算物理實驗內容<br>
      使用程式計算手算困難的單擺運動<br>
      測試*不同積分方法*會不會明顯影響實驗結果<br>
      並實驗計算量只多個幾倍，準確度卻能提高千倍萬倍的榮格-庫塔（Runge-Kutta）方法<br><br>
  - 如何做到那件事？<br>
      用vpython繪製一個大平面(天花板)，一條擺繩，跟一個擺錘<br>
      給定兩球的角度、重量、半徑以及重力常數與榮格-庫塔方法後作運算[程式碼](/第二堂課-單擺運動2/單擺運動二.py)<br>
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
  - 做出來的結果<br><br>
      ![This is an image](/第二堂課-單擺運動2/result.png)<br>
      <br>
      上圖是使用榮格-庫塔法做積分得到的結果<br>
      比起前面的矩形或梯形法擁有更高的精確度<br>
      線條幾乎沒有變粗，放大一點看<br><br>
      ![This is an image](/第二堂課-單擺運動2/resultdtc.png)<br>
      <br>
      ![This is an image](/第二堂課-單擺運動2/resultddtc.png)<br>
      <br>
      ![This is an image](/第二堂課-單擺運動2/resultd3tc.png)<br>
      <br>
      看起來榮格-庫塔法幾乎沒有誤差，取位置的絕對值恆為1<br>
  - 結論<br>
      經過python的作圖分析結果，得知`榮格-庫塔方法`**能以簡單計算獲得能接受的結果**
