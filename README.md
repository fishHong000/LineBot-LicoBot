# LineBot-LicoBot

## LINE bot建立：
到Line Developers建立一個Messaging API的機器人。

## Python套件安裝:
	至CMD進行安裝定時爬蟲所需套件
	pip install beautifulsoup4
	pip install requests
	pip install pandas
	pip install psycopg2
	pip install schedule
	pip install time

## node.js套件安裝:
	先到node.js官網下載node.js
	安裝好後在CMD頁面切到專案資料夾下
	安裝pg、heroku、dialogflow、dialogflow-fulfillment、@line/bot-sdk、linebot

	npm install pg
	npm install heroku
	npm install dialogflow
	npm install dialogflow-fulfillment
	npm install @line/bot-sdk
	npm install linebot

Dialogflow串接到LINE bot:
	首先要先註冊一個Dialogflow帳號，並且新增一個Agent
	完畢後切換到Integrations，滑到Text based的地方有LINE可以選擇
	點進去後就可以填入Channel ID、Channel Secret、Channel Access Token
	並將此處的Webhook URL複製起來貼到LINE Developers/Messaging API的Webhook URL中
	即串接完成。
	此時就可以在Dialogflow上建立意圖、回覆。

## Heroku串接Dialogflow:
	在Heroku的指定app頁面點開open app，並將上方網址複製下來
	回到Dialogflow的fulfillment處將網址貼到URL的部分
	並在網址後方加上/dialogflow
	此處是對應到程式碼index.js的第16行

## 程式碼串接資料庫:
	先到Heroku上建立一個PostgreSQL，切換到PostgreSQL的設定頁面
	將URI複製起來，接著貼到程式碼檔案裡utility/asyncDB.js裡的pgConn
	接著再到資料庫創建對應名稱的資料庫，也可以在程式碼裡自行修改SQL指令中的資料表名稱

## 開發程式碼之安裝設定:
	1.解壓縮"程式碼.zip"的檔案並將LicoBot資料夾解壓縮至指定位置

	2.先創辦一個Heroku帳號，新增一個app放置程式碼
	  
	3.用cmd切到專案資料夾下
	並依序輸入
	heroku login //登入Heroku
	heroku git:remote -a "APP的名字" //讓程式碼上傳到Heroku上指定的app中
	git init //初始化 Git 
	git add . //將要推上去的檔案加到清單中
	git commit -am "myApp" //為本次的push加上註解
	git push heroku main //將檔案推上heroku

	即可完成安裝。
