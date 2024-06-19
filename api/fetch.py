
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd

import os
from time import time, sleep



def read_json_and_return(filename): 
    """
    Reads JSON data from a file or returns None if the file is not found.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        dict: The parsed JSON data, or None if the file is not found.
    """

    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: JSON file '{filename}' not found. ")
        return None



def api_exec():
    """
    Fetch the latest cryptocurrency data from CoinMarketCap API, process it into a pandas DataFrame,
    save the JSON response to a file, and append the data to a CSV file.

    Returns:
    list of dict: Processed cryptocurrency data.
    """
    global df

    # CoinMarketCap API endpoint
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    
    # API request parameters
    parameters = {
        'start': '1',
        'limit': '10',
        'convert': 'USD'
    }
    
    # API request headers
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'c6b393db-6b8c-4faf-8cb5-4e918e116472',  # Replace with your actual API key
    }

    # Create a session and update headers
    session = Session()
    session.headers.update(headers)

    try:
        # Send GET request to the API
        response = session.get(url, params=parameters)
        data = json.loads(response.text)

        # Save the JSON response to a file
        file_path = 'data.json'
        with open(file_path, 'w') as file:
            json.dump(data, file)
            

        # Process data
        # Configure pandas display options: max columns, values/decimal places, 
        pd.set_option('display.max_columns', None)
        pd.set_option('display.float_format', lambda x: '%.2f' % x)

        # Normalize JSON data into a DataFrame
        df = pd.json_normalize(data['data'])
        df['timestamp'] = pd.to_datetime('now')

        # Concatenate DataFrame with itself for demonstration purposes
        # df = pd.concat([df2, df2], ignore_index=True)
        df['timestamp'] = df['timestamp'].astype(str)  # Convert Timestamp to string


        # Convert DataFrame to a list of dictionaries
        crypto_data = df.to_dict(orient='records')

        # Append the DataFrame to a CSV file
        csv_path = 'api.csv'
        if not os.path.isfile(csv_path):
            df.to_csv(csv_path, header=True, index=False)
        else:
            df.to_csv(csv_path, mode='a', header=False, index=False)

        return crypto_data
    
    # for i in range(333):
    #     print(api_exec())
    #     print('\nAPI execution completed')
    #     sleep(60)  # Wait for 60 seconds before the next iteration

    # exit()

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(f'Error: API request failed: {e}')
    
        file_path = 'data.json'
        #Load local data
        data = read_json_and_return(file_path)
        if data:
            print("API unreachable, using saved data from data.json")

            
            pd.set_option('display.max_columns', None)
            pd.set_option('display.float_format', lambda x: '%.2f' % x)

            df = pd.json_normalize(data['data'])
            df['timestamp'] = pd.to_datetime('now')

            df['timestamp'] = df['timestamp'].astype(str)  # Convert Timestamp to string

            # Convert DataFrame to a list of dictionaries
            crypto_data = df.to_dict(orient='records')
            return crypto_data
        
        else:
            print("Both API and saved data unavailable.")
            return None    
        

    