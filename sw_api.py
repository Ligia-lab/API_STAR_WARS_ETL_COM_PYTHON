import requests
import pandas as pd
import sqlite3


class SWExtraction:
    
    def __init__(self, api_url):
        self.api_url = api_url
        
        self.results = []
        
        
    def fetch_data(self):
        url = self.api_url
        
        while url:
            response = requests.get(url, verify=False)
            if response.status_code != 200:
                raise Exception('Falha ao acessar dados')
            
            
            data = response.json()
            itens = data.get('results', [])
            
            for p in itens:
                pop = p.get('population', 'unknown')
                if not pop.isnumeric():
                    pop_val = None
                else:
                    pop_val = int(pop)
                    
                planeta_dict = {
                    'name': p.get('name'),
                    'climate': p.get('climate'),
                    'terrain': p.get('terrain'),
                    'population': pop_val
                }
                self.results.append(planeta_dict)
                
            url = data.get('next')
            
        
        
    