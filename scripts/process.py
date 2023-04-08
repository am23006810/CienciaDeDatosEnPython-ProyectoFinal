import numpy as np
import pandas as pd

def data_processing(red_data, rose_data, white_data):
    red_data['type'] = 'Red'
    rose_data['type'] = 'Rose'
    white_data['type'] = 'White'
    complete_df = pd.concat([red_data,rose_data,white_data], ignore_index = True)
    complete_df.loc[ complete_df['year'] == 'N.V.', 'year'] = 0
    complete_df['year'] = complete_df['year'].astype(int)
    complete_df['name'] = complete_df['name'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    complete_df['winery'] = complete_df['winery'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    return complete_df