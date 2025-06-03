from sw_api import SWExtraction
import pandas as pd

url = 'https://swapi.dev/api/planets/'

extract = SWExtraction(api_url=url)
extract.fetch_data()

for planeta in extract.results[:3]:
    print(planeta)

    
df = extract.to_dataframe()
print(df.head())