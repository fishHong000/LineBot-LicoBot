'use strict';

//-----------------------
// 引用資料庫模組
//-----------------------
const {Client} = require('pg');

//-----------------------
// 自己的資料庫連結位址
//-----------------------
var pgConn = 'postgres://knpdgykkdjenvo:2f275de5fc59d8162428582e6774335b0d31c89808ce425ef71be2314ae1859c@ec2-3-218-171-44.compute-1.amazonaws.com:5432/dd0ktn67rn598o';


//產生可同步執行query物件的函式
function query(sql, value=null) {
    return new Promise((resolve, reject) => {
        //設定資料庫連線物件
        var client = new Client({
            connectionString: pgConn,
            ssl: true
        })     

        //連結資料庫
        client.connect();

        //回覆查詢結果  
        client.query(sql, value, (err, results) => {                   
            if (err){
                reject(err);
                console.log(err);
            }else{
                resolve(results);
            }

            //關閉連線
            client.end();
        });
    });
}

//匯出
module.exports = query;