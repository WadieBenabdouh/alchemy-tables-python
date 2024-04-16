import requests
import pandas
import sqlalchemy
from sqlalchemy import create_engine

url = "https://www.cheapshark.com/api/1.0/deals?upperPrice=15"
header = {'Content_Type' : "application/json", 'Accept-Encoding':"Deflate"}

response = requests.get(url, headers=header)
responseData = response.json()
df = pandas.json_normalize(responseData)

engine = create_engine('postgresql://postgres:main@localhost:5432/games-prices')
df.to_sql(name='GamePrices', con=engine, index=False, if_exists='fail')
# print(df)

# from where I learned this :
# https://www.youtube.com/watch?v=Sw79_adeUR0&t=109s