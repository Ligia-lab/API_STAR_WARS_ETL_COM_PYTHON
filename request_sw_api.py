from sw_api import SWExtraction

url = 'https://swapi.dev/api/planets/'

extract = SWExtraction(api_url=url)
extract.fetch_data()

for planeta in extract.results:
    print(planeta)

    
