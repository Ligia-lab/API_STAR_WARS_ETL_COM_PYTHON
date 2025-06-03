import requests
import pandas as pd
import sqlite3


class SWExtraction:
    
    def __init__(self, api_url):
        self.api_url = api_url
        