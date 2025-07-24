//----------------------------------------
// 載入必要的模組
//----------------------------------------
var express = require('express');
const { WebhookClient } = require('dialogflow-fulfillment');
const app = express();

//增加引用函式
const confirmedAmount = require('./utility/confirmedAmount');



//--------------------------------
// 機器人接受訊息的處理
//--------------------------------
app.post('/dialogflow', express.json(), (req, res) => {
    //------------------------------------
    // 處理請求/回覆的Dialogflow代理人
    //------------------------------------  
    const agent = new WebhookClient({ request: req, response: res });

    
    function getConfirmedAmount() {
        return confirmedAmount.fetchConfirmedAmount().then(data => {
            if (data == -1) {
                agent.add('找不到資料');
            } else if (data == -9) {
                agent.add('執行錯誤');
            } else {
                agent.add(data.year + "/" + data.month + "/" + data.date + "：\n" + data.content);
            }
        })
    }

let intentMap = new Map();
//------------------------------------
intentMap.set('getConfirmedAmount', getConfirmedAmount);
//------------------------------------
agent.handleRequest(intentMap);         
});



//----------------------------------------
// 監聽3000埠號, 
// 或是監聽Heroku設定的埠號
//----------------------------------------
var server = app.listen(process.env.PORT || 3000, function () {
    const port = server.address().port;
    console.log("正在監聽埠號:", port);
});