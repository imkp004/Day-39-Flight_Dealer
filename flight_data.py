class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


    def find_cheapest_flight(self, flights_Data):

        if len(flights_Data['data']) == 0:
            # return f"N/A"
            return f"{0.0}"
        elif len(flights_Data['data']) == 1:
            first_flight = flights_Data['data'][0]
            lowest_price = float(first_flight["price"]["grandTotal"])
            return lowest_price
        else:
            first_flight = flights_Data['data'][0]
            lowest_price = float(first_flight["price"]["grandTotal"])
            self.origin_airport = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            self.destination_airport = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            self.out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            self.return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

            for each in flights_Data['data']:
                self.price = float(each["price"]["grandTotal"])
                if lowest_price > self.price:
                    lowest_price = self.price

                self.origin_airport = each["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                self.destination_airport = each["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                self.out_date = each["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                self.return_date = each["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

            return [lowest_price, self.origin_airport, self.destination_airport, self.out_date, self.return_date]