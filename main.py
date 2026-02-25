#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import *

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

sheet = DataManager()
flight = FlightSearch()
flight_data_managing = FlightData("N/A", "N/A", "N/A", "N/A", "N/A", 0)
message = NotificationManager()

sheet_data = sheet.get_data()
sheet_user_data = sheet.get_users_emails()
user_email_list = [each['E-mail'] for each in sheet_user_data]
user_phone_list = [each['Phone Number'] for each in sheet_user_data]

departure = datetime.today() + timedelta(days=30)
returning = departure + timedelta(days=20)

for each in sheet_data:

    if each['iataCode'] != flight.get_destination_code(each['city']) or each['iataCode'] == '':
        each['iataCode'] = flight.get_destination_code(each['city'])
        sheet.update_data(each)

    flights_Data = flight.get_flights_price(each['iataCode'], departure.strftime("%Y-%m-%d"),
                                            returning.strftime("%Y-%m-%d"))

    flights_list = flight_data_managing.find_cheapest_flight(flights_Data)
    # print(f"Getting flights for {each['city']}...")
    # print(f"{each['city']}: ${flights_list[0]}")

    each['todayPrice'] = flights_list[0]
    sheet.update_data(each)

    if (float(each["lowestPrice"]) >= float(each["todayPrice"])) and (float(each["todayPrice"]) != 0):
        message.send_text(user_phone_list, flights_list[0], flights_list[1], flights_list[2], flights_list[3], flights_list[4], flights_list[5])
        message.send_emails(user_email_list, flights_list[0], flights_list[1], flights_list[2], flights_list[3], flights_list[4], flights_list[5])
