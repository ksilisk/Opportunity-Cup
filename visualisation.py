import json
import streamlit as st
import pandas as pd


def visualisation():
    with open('transactions.json') as json_file:
        data = json.load(json_file)
        data = data['transactions']
        data = data
        result = pd.DataFrame.from_dict(data).T
        result.index = result.index.astype(int)
        result['amount'] = result['amount'].astype(int)
        result['date'] = pd.to_datetime(result['date'], format='%Y-%m-%dT%H:%M:%S')
        result['account_valid_to'] = pd.to_datetime(result['account_valid_to'], format='%Y-%m-%d')
        result['date_of_birth'] = pd.to_datetime(result['date_of_birth'], format='%Y-%m-%d')
        result['passport_valid_to'] = pd.to_datetime(result['passport_valid_to'], format='%Y-%m-%d')
        print(result.dtypes)
        st.write(result)


if __name__ == '__main__':
    visualisation()