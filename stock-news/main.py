import os
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "RLROMMP9SZU28032"
NEWS_API_KEY = "b76bb57b31d24b5486b59e6b26ef0458"
account_sid = os.getenv('TWILIO_ACCOUNT_SID')

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

news_params = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "pageSize": 3
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()
time_series = stock_data['Time Series (Daily)']
dates = sorted(time_series.keys(), reverse=True)
yesterday_closing_price = float(time_series[dates[1]]['4. close'])
day_before_yest_price = float(time_series[dates[2]]['4. close'])

abs_diff = abs(yesterday_closing_price - day_before_yest_price)
abs_percentage_diff = (abs_diff / day_before_yest_price) * 100
perc_diff = (yesterday_closing_price - day_before_yest_price)/day_before_yest_price*100

if abs_percentage_diff > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()
    articles = news_data['articles']

    first_three_articles = [{"headline": article['title'], "description": article['description']} for article in articles[:3]]

    auth_token = os.getenv('AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    for article in first_three_articles:
        message_body = f"TSLA: {'🔺' if perc_diff > 0 else '🔻'}{perc_diff:.2f}%\nHeadline: {article['headline']}\nBrief: {article['description']}"
        message = client.messages.create(
            body=message_body,
            from_="whatsapp:+14155238886",
            to="whatsapp:+14086181185",
        )
        print(f"Message sent: {message.sid}")

# Print the absolute difference and percentage difference
print(f"Absolute difference: {abs_diff}")
print(f"Percentage difference: {perc_diff:.2f}%")

# Optional: Format the message
for article in first_three_articles:
    formatted_message = f"""
    TSLA: {'🔺' if perc_diff > 0 else '🔻'}{perc_diff:.2f}%
    Headline: {article['headline']}
    Brief: {article['description']}
    """
    print(formatted_message)
