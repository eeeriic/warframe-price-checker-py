import pandas as pd
from prices import get_average_price

def build_price_df(item_list, price_func=get_average_price):
    df = pd.DataFrame(item_list)
    df = df.rename(columns={"item_name": "item_name"})
    df['avg_price'] = df['item_name'].apply(price_func)
    return df.sort_values(by='avg_price', ascending=False).reset_index(drop=True)

