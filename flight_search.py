import requests
import os
from dotenv import load_dotenv
load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.environ.get("flight_deal_search_key")
        self.api_secret = os.environ.get("flight_deal_search_secret")
        self.token = self.get_new_token()


    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

        parameter = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        header = {
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.get(url=url, params=parameter, headers=header)
        try:
            code = response.json()["data"][0]['iataCode']
            return code
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"




    def get_new_token(self):
        url = 'https://test.api.amadeus.com/v1/security/oauth2/token'
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }

        response = requests.post(url=url, headers=header, data=data)
        return response.json()['access_token']



    def get_flights_price(self, destination_Location_Code, departure_Date, return_Date):
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        parameter = {
            "originLocationCode": "BOS",
            "destinationLocationCode": destination_Location_Code,
            "departureDate": departure_Date,
            "returnDate": return_Date,
            "adults": 1,
            "currencyCode": "USD",
            "nonStop": 'true',
        }

        header = {
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.get(url=url, params=parameter, headers=header)
        return response.json()
