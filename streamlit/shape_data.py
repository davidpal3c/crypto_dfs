import pandas as pd
import json

def main_df():
    data = 'data.json'
    with open(data, 'r') as file:
        data = json.load(file)


    df = pd.json_normalize(data['data'])

    return df