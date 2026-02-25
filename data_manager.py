import requests
from dotenv import load_dotenv
import os
load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url1 = os.environ.get("google_sheet_url")
        self.url2 = os.environ.get("google_users_sheet_url")
        self.auth_username = os.environ.get("google_sheet_username")
        self.auth_password = os.environ.get("google_sheet_password")

    def get_data(self):
        # response = requests.get(url=self.url, auth=(self.auth_username, self.auth_password))
        # return response.json()['prices']
        response = requests.get(url=self.url1)
        return response.json()

    def get_users_emails(self):
        response = requests.get(url=self.url2)
        return response.json()

    def update_data(self, each_item):
        # to_update = f"{self.url}/{each_item['id']}"
        to_update = f"{self.url1}/city/{each_item['city']}"
        body = {
            'iataCode': each_item['iataCode'],
            'todayPrice': each_item['todayPrice']
            }
        header = {
            "Content-Type": "application/json"
        }

        # response = requests.put(url=to_update, json=body)
        response = requests.patch(url=to_update, headers=header, json=body)
