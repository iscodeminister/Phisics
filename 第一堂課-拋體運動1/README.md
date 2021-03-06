# 第一堂課-拋體運動
## Task lists
- [x] 我們都知道【45° 拋射距離最遠】這件事，確認一下程式的模擬結果是不是真的 45° 拋射最遠。
- [x] 丟鉛球的時候，鉛球出手的地方應該在頭部附近，絕對不是從地板開始，這樣的話還是 45° 拋射最遠嗎？用你的程式丟看看結果如何？
## 報告
### 1.無空氣阻力
  - 要做到什麼事？<br>
      使用`python`的外掛`vpython`來模擬繪製與計算物理實驗內容<br>
      測試*只考慮重力*時將圓球**以45度拋射**是否為最遠<br><br>
  - 如何做到那件事？<br>
      用vpython繪製一個平面(地板)，一個待發射的球體，並指定5種不同的角度(15的倍數)<br>
      給定球的初速以及重量以及重力常數後作運算[程式碼](/第一堂課-拋體運動1/拋體運動一csv.py)<br>
      ```ball.pos.x = -floor.length/2
	  ball.pos.y = ball.radius+floor.height/2
	  ball.y0 = ball.pos.y
	  ball.m = 0.1 
	  ball.v0 = 10
      ``` 
      運算完之後以以圖表確認並輸出csv紀錄實驗數據<br><br>
  - 做出來的結果<br>
      ![This is an image](/第一堂課-拋體運動1/實驗成果.png)<br>
      以紅(15°)，綠(30°)，紫(45°)，藍(60°)，白(75°)線段表示球的移動軌跡<br>
      參考此圖，發現**45度拋出的球應是最遠**，30與60度、15與70度的落點大致相同<br>
      ~~因為無聊~~為求正確，又改了一段程式碼使其跑1至89度的模擬並比對輸出的[csv](/第一堂課-拋體運動1/out2.csv)檔<br><br>
      ![This is an image](/第一堂課-拋體運動/實驗成果2.png)<br>
      以高為180cm之長方體為假人<br>
      紅(15°)，綠(30°)，紫(45°)，藍(60°)，白(75°)線段表示球的移動軌跡<br>
      ~~參考此圖，發現**45度拋出的球應是最遠**，但此時30°、60°與15°、70°的落差較為明顯<br>
      在低角度時球的落點較為遠，我推測是因為y方向初始高度較高<br>
      低角度時y分量較低但x分量較高導致出現此觀測結果~~<br>
      本來是這麼想的，但思考一下之後發現有邏輯漏洞<br>
      所以又改了一下[程式碼](/第一堂課-拋體運動1/拋體運動一hw2csv1to89.py)，發現最遠的角度竟**不是45°**<br>
      ![This is an image](/第一堂課-拋體運動1/實驗成果3.png)<br>
      以綠色軌跡代表45°，作圖之後發現<br>
      ![This is an image](/第一堂課-拋體運動1/細部45.png)<br>
      45度竟沒有最遠，檢查輸出的[csv](/第一堂課-拋體運動1/out4.csv)<br>
      發現最遠出現在41°時在11.86856公尺處，比45°時的11.76626公尺更遠<br><br>

  - 結論<br>
      經過python的作圖分析與csv之數據比對結果，得知`在不考慮空氣阻力以及在初始高度為零的情況下`**45° 拋射距離最遠**