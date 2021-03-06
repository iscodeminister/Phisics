# 第二堂課-單擺運動三
## Task lists
- [x] 改變圓錐擺的初始速度（速率、方向等），觀察運動軌跡有什麼變化？簡短描述自己的觀察結果。
## 報告
### 1.單擺運動一 歐拉法
  - 要做到什麼事？<br>
      使用`python`的外掛`vpython`來模擬繪製與計算物理實驗內容<br>
      使用程式計算手算困難的單擺運動<br>
      測試*改變初始值*會不會明顯影響實驗結果<br><br>
  - 如何做到那件事？<br>
      用vpython繪製一個大平面(天花板)，一條擺繩，跟一個擺錘<br>
      給定兩球的角度、重量、半徑以及重力常數後作運算[程式碼](/第二堂課-單擺運動3/單擺運動二改三.py)<br>
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
      一開始時把程式碼都打上發現<br>
      ![This is an image](/第二堂課-單擺運動3/result1-1.png)<br>
      出現了一個神奇的籃子，後來經過討論並修改了程式碼之後<br>
      ![This is an image](/第二堂課-單擺運動3/result.png)<br>
      <br>
      放大一點看<br>
      ![This is an image](/第二堂課-單擺運動3/result2.png)<br>
      發現theta角決定了圓的起伏狀態<br><br>
  - 結論<br>
      經過python的作圖分析結果，得知藉由`改變圓錐擺的初始速度`**可以改變圖形的運動狀態**