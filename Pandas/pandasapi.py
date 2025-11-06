import pandas as pd

df = pd.read_json("https://dummyjson.com/recipes")
print(df.info())
print(df['recipes'].loc[:0])