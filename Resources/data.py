import pandas as pd

cities_df = pd.read_csv("cities.csv")

cities_html = cities_df.to_html()

print(cities_html)