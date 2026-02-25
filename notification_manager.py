from dotenv import load_dotenv
import os
import requests
load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send(self, Price, Departure_Airport_IATA_Code, Arrival_Airport_IATA_Code, Outbound_Date, Inbound_Date):

        url = os.environ.get("twillo_url")

        message_body = f"Low price alert! ✈️Only £{Price} to fly from {Departure_Airport_IATA_Code} to {Arrival_Airport_IATA_Code}From {Outbound_Date} to {Inbound_Date}"

        response = requests.post(
            url,
            auth=(os.environ.get("twillo_sid"), os.environ.get("twillo_auth_token")),
            data={
                "From": os.environ.get("twillo_phone"),
                "To": os.environ.get("my_phone"),
                "Body": message_body
            }
        )

        print(response.status_code)
        print(response.json())