from dotenv import load_dotenv
import os
import requests
load_dotenv()
import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_text(self, user_phone_list, Price, Departure_Airport_IATA_Code, Arrival_Airport_IATA_Code, Outbound_Date, Inbound_Date, stops):

        # print(f"Low price alert! ✈️Only ${Price} to fly from {Departure_Airport_IATA_Code} to {Arrival_Airport_IATA_Code} From {Outbound_Date} to {Inbound_Date} with {stops} stops in between")

        for phone in user_phone_list:
            url = os.environ.get("twillo_url")
            message_body = f"Low price alert! ✈️Only £{Price} to fly from {Departure_Airport_IATA_Code} to {Arrival_Airport_IATA_Code}From {Outbound_Date} to {Inbound_Date}"

            response = requests.post(
                url,
                auth=(os.environ.get("twillo_sid"), os.environ.get("twillo_auth_token")),
                data={
                    "From": os.environ.get("twillo_phone"),
                    "To": f"+{phone}",
                    "Body": message_body
                }
            )

            # print(response.status_code)
            # print(response.json())

    def send_emails(self, user_list, Price, Departure_Airport_IATA_Code, Arrival_Airport_IATA_Code, Outbound_Date, Inbound_Date, stops):

        # for email in user_list:
        #     print(f"Subject:Cheap Flight Deal\n\nLow price alert! ✈️Only ${Price} to fly from {Departure_Airport_IATA_Code} to {Arrival_Airport_IATA_Code} From {Outbound_Date} to {Inbound_Date} with {stops} stops in between")

        for email in user_list:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=os.environ.get('my_email'), password=os.environ.get('password'))
                connection.sendmail(from_addr=os.environ.get('my_email'),
                                    to_addrs=email,
                                    msg=f"Subject:Cheap Flight Deal\n\nLow price alert! Only ${Price} to fly from {Departure_Airport_IATA_Code} to {Arrival_Airport_IATA_Code} From {Outbound_Date} to {Inbound_Date} with {stops} stops in between")
