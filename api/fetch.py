
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd



url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'15',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'c6b393db-6b8c-4faf-8cb5-4e918e116472',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
#   print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


# save json_data to file:
# file_path = 'data.json'
# with open(file_path, 'w') as file:
#   json.dump(data, file)


# pd.set_option('display.max_columns', None)

df = pd.json_normalize(data['data'])
df['timestamp'] = pd.to_datetime('now')

# print(df.head())
data = df.to_dict(orient='records')
crypto_df = data

