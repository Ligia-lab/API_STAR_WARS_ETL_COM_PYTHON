import requests
import pandas as pd
import sqlite3


class SWExtraction:
    
    def __init__(self, api_url):
        self.api_url = api_url
        
        self.results = []
        
        
    def fetch_data(self):
        response = requests.get(self.api_url, verify=False)
        if response.status_code == 200:
            self.results = response.json().get('results', [])
            print('Dados recebidos')
        else:
            raise Exception('Falha ao acessar dados')