from dotenv import load_dotenv
import os
load_dotenv('/home/pedro/TheSuperAnalyst/config/enviroments/api-config.env')
class ApiConfig:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')