import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla INC"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "2UIMN6A74LL88KWY"
NEWS_API_KEY = "71d062bde9114641a69d272d5ec30098"

TWILIO_SID = "AC14aa67dd5720e3a08ba9931b82cc2352"
TWILIO_AUTH_TOKEN = 'ab9398d4b007c9c2e4efaf5d51177d4d'


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None

if difference > 0:
    up_down = "⬆"
else:
    up_down = "⬇"

diff_percent = (difference / float(yesterday_closing_price)) * 100

if abs(diff_percent) < 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)

formatted_articles = {f"{STOCK_NAME}: {up_down}{diff_percent}\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles}
print(formatted_articles)
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
# for article in formatted_articles:
#     message = client.messages.create(
#         body=article,
#         from_="+17176475903",
#         to="+15122101474"
# )
