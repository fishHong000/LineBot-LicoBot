# 安裝套件
import requests
import pandas as pd
from bs4 import BeautifulSoup
import psycopg2
import schedule
import time

def reptile():
    # 到衛生福利部疾病管制署擷取最新當日確診人數
    response = requests.get(
        "https://www.cdc.gov.tw/")
    soup = BeautifulSoup(response.text, "html.parser")
    YearMonth = soup.find_all("p", class_ = "icon-year")
    Date = soup.find_all("p", class_ = "icon-date")
    content0 = soup.find_all("div", class_ = "content-boxes-in-v3 JQsummary")
    
    # 整理抓取下來的資料
    i = 0
    while (i < len(content0)):
        if "例COVID-19確定病例，分別為" in content0[i].text.replace("\n", ""):
            content1 = content0[i].text.replace("\n", "")
            
            # 擷取年月
            getYearMonth = YearMonth[i].text.replace(" ", "").replace("-", "")
            
            # 取得日期
            getDate = Date[i].string
            Date0 = getDate.split()
            Date = " ".join(str(i) for i in Date0)
            
            # 取得年分
            getYear = ""
            for i in range(4):
                getYear = getYear + getYearMonth[i]
            Year0 = getYear.split()
            Year = " ".join(str(i) for i in Year0)
            
            # 取得月份
            getMonth = ""
            for j in range(4, len(getYearMonth)):
                getMonth = getMonth + getYearMonth[j]
                Month0 = getMonth.split()
                Month = " ".join(str(i) for i in Month0)
            
            i = len(content0)
            
        else:
            i += 1
            
    news0 = content1.split()
    news = " ".join(str(i) for i in news0)
    
    # 將資料放到Postgre SQL
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(database = "dd0ktn67rn598o", user = "knpdgykkdjenvo", password = "2f275de5fc59d8162428582e6774335b0d31c89808ce425ef71be2314ae1859c",
                host = "ec2-3-218-171-44.compute-1.amazonaws.com", port = "5432")
        print ("Opened database successfully")
        
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS confirmed_amount")
        cur.execute('''CREATE TABLE confirmed_amount
            (
            YEAR            varchar(4)   NOT NULL,
            MONTH           varchar(2)        NOT NULL,
            DATE            varchar(2)   NOT NULL,
            CONTENT            varchar(50)   NOT NULL);''')
        print("Table created successfully")
        
        insert_script = "INSERT INTO confirmed_amount (YEAR, MONTH, DATE, CONTENT) VALUES (%s, %s, %s, %s)"
        insert_value = (Year, Month, Date, news)
        cur.execute(insert_script, insert_value)
        conn.commit()
        cur.close()
        
    except Exception as error:
        print(error)
        
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
            
    print("reptile, ok!")

# 設定每小時取一次資料
schedule.every().hour.do(reptile)

while 1:
    schedule.run_pending()
    time.sleep(1)