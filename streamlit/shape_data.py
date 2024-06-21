import pandas as pd
import numpy as np
import json

# data = pd.read_csv('data.csv')
# st.write(data)



def main_df():
    data = 'data.json'
    with open(data, 'r') as file:
        data = json.load(file)

    df = pd.json_normalize(data['data'])

    return df




# create class chartIt feeding on json and provoding methods (bar chart, line chart, etc.)