import dotenv
import os

dotenv.load_dotenv()

NEWS_API_KEY=os.getenv('NEWS_API_KEY')  
STOCK_API_KEY=os.getenv('STOCK_API_KEY') 

STOCK_NAME = "AAPL"
COMPANY_NAME = "apple inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parms={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY,

}

import requests

response=requests.get(STOCK_ENDPOINT,params=stock_parms)
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]
yesterday_data=data_list[0]["4. close"]
# print(yesterday_data)

day_before_yesterday_data=data_list[1]["4. close"]
# print(day_before_yesterday_data)

difference=abs(float(yesterday_data)-float(day_before_yesterday_data))
diff_percent=round((difference/float(day_before_yesterday_data))*100)
# print(diff_percent)



news_parms={
    "q":COMPANY_NAME,
    "apiKey":NEWS_API_KEY,
}
response=requests.get(NEWS_ENDPOINT,params=news_parms)
article=response.json()["articles"][:3]
if (float(yesterday_data)-float(day_before_yesterday_data))>0:

    up="UP^^"
else:
    up="DOWN!!"

formated_article=f"{STOCK_NAME}: {up} {diff_percent}% \nHeadline: {article[0]['title']}. \nBrief: {article[0]['description']}"
print(formated_article)


