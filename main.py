#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.



import requests
from pprint import pprint
from datetime import *

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

sheet = DataManager()
flight = FlightSearch()
flight_data_managing = FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

sheet_data = sheet.get_data()

departure = datetime.today() + timedelta(days=1)
returning = departure + timedelta(days=6*30)
for each in sheet_data:

    if each['iataCode'] != flight.get_destination_code(each['city']) or each['iataCode'] == '':
        each['iataCode'] = flight.get_destination_code(each['city'])
        sheet.update_data(each)


    flights_Data = flight.get_flights_price(each['iataCode'], departure.strftime("%Y-%m-%d"),
                                            returning.strftime("%Y-%m-%d"))

    print(f"Getting flights for {each['city']}...")
    print(f"{each['city']}: ${flight_data_managing.find_cheapest_flight(flights_Data)}")

    each['lowestPrice'] = f"${flight_data_managing.find_cheapest_flight(flights_Data)}"
    sheet.update_data(each)



