# TronClass2Excel
將TronClass的學生名單及成績匯出成xlsx或csv

## 動機
由於TronClass不像舊有的iCan系統能匯出Excel，非常不方便，因此就寫了簡單的程式來匯出成Excel或是csv。

## 使用教學
#### 輸出TronClass的學生名單
1. 先到課程的班級成員頁面
2. 右鍵另存網頁並將檔名命名為`student`，請選擇完整網頁
3. 此時下載的應該會有個資料夾及一個`student.htm`的檔案
4. 將`student.htm`此檔案放到此專案的目錄夾下

**輸出 csv**
```
$ python3 student2csv.py
```

**輸出 Excel**
```
$ python3 student2xlsx.py
```
![alt text](https://s19.postimg.org/gu2ak6mmr/2018-01-19_11.22.31.png "班級成員頁面")

#### 輸出TronClass的學生作業成績
1. 先到課程的作業成績頁面 > 選擇要輸出成績的作業 > 點選作業批改頁面
2. 右鍵另存網頁並將檔名命名為`score`，請選擇完整網頁
3. 此時下載的應該會有個資料夾及一個`score.htm`的檔案
4. 將`score.htm`此檔案放到此專案的目錄夾下

**輸出 csv**
```
$ python3 score2csv.py
```

**輸出 Excel**
```
$ python3 score2xlsx.py
```
![alt text](https://s19.postimg.org/bwopyufg3/2018-01-19_11.50.43.png "作業成績頁面")


## Contribute
Contributions are always welcome!
