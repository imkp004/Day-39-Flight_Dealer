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
            return f"N/A"
        elif len(flights_Data['data']) == 1:
            first_flight = flights_Data['data'][0]
            lowest_price = float(first_flight["price"]["grandTotal"])
            return lowest_price
        else:
            first_flight = flights_Data['data'][0]
            lowest_price = float(first_flight["price"]["grandTotal"])
            # origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            # destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            # out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            # return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            #
            for each in flights_Data['data']:
                self.price = float(each["price"]["grandTotal"])
                if lowest_price > self.price:
                    lowest_price = self.price

            return lowest_price