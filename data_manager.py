import requests
from dotenv import load_dotenv
import os
load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = os.environ.get("google_sheet_url")
        self.auth_username = os.environ.get("google_sheet_username")
        self.auth_password = os.environ.get("google_sheet_password")

    def get_data(self):
        response = requests.get(url=self.url, auth=(self.auth_username, self.auth_password))
        return response.json()['prices']

    def update_data(self, each_item):
        to_update = f"{self.url}/{each_item['id']}"
        body = {
            "price": {
                'iataCode': each_item['iataCode'],
                'lowestPrice': each_item['lowestPrice']
            }
        }

        response = requests.put(url=to_update, json=body, auth=(self.auth_username, self.auth_password))
