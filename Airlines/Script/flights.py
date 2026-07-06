# ===========================================
# flights.py
# ===========================================


from aircrafts import AircraftGenerator
import random
import pandas as pd
import os

from config import *
from utils import *


class FlightGenerator:

    def __init__(self):

        self.airlines = AIRLINES
        self.airports = AIRPORTS

        aircraft_generator = AircraftGenerator()

        self.aircraft_data = aircraft_generator.generate_dataset().to_dict("records")

    # ---------------------------------------

    def generate_flight_information(self, flight_id):

        airline = random.choice(self.airlines)

        aircraft = random.choice(self.aircraft_data)

        flight_info = {

            "FlightID": f"FL{flight_id:07d}",

            "FlightNumber": generate_flight_number(),

            "Airline": airline,

            "AircraftID": aircraft["AircraftID"]

        }

        return flight_info, aircraft

    # ---------------------------------------

    def generate_route(self):

        origin = random.choice(self.airports)

        destination = random.choice(

            [airport for airport in self.airports if airport != origin]

        )

        distance = random_distance()

        return {

            "OriginAirportID": origin["AirportID"],
            "OriginAirportCode": origin["Code"],
            "OriginAirportName": origin["AirportName"],
            "OriginCity": origin["City"],

            "DestinationAirportID": destination["AirportID"],
            "DestinationAirportCode": destination["Code"],
            "DestinationAirportName": destination["AirportName"],
            "DestinationCity": destination["City"],

            "DistanceKM": distance

        }
    # ---------------------------------------

    def generate_schedule(self, distance, aircraft):

        # Random flight date
        flight_date = random_date()

        # Realistic departure time
        hour, minute = generate_departure_time()

        scheduled_departure = flight_date.replace(
            hour=hour,
            minute=minute
        )

        # Average cruising speed (Version 1)
        average_speed = aircraft["CruiseSpeed"]

        # Flying time in minutes
        air_time = int((distance / average_speed) * 60)

        # Add taxi and operational buffer
        flight_duration = air_time + random.randint(15, 30)

        scheduled_arrival = scheduled_departure + timedelta(
            minutes=flight_duration
        )

        return {

            "FlightDate": flight_date,

            "ScheduledDeparture": scheduled_departure,

            "ScheduledArrival": scheduled_arrival,

            "FlightDurationMinutes": flight_duration,

            "AirTimeMinutes": air_time,

            "Terminal": random_terminal(),

            "Gate": random_gate(),

            "TaxiOutMinutes": generate_taxi_out(),

            "TaxiInMinutes": generate_taxi_in(),

            "RecordCreatedAt": generate_record_timestamp(),

            "FlightType": "Domestic",

            "DayOfWeek": flight_date.strftime("%A"),

        }

    # ---------------------------------------

    def generate_weather(self):

        weather = random_weather()

        if weather == "Clear":

            temperature = random.randint(28, 40)
            humidity = random.randint(35, 60)
            visibility = random.randint(8, 10)
            wind_speed = random.randint(5, 20)

        elif weather == "Cloudy":

            temperature = random.randint(22, 34)
            humidity = random.randint(55, 80)
            visibility = random.randint(6, 9)
            wind_speed = random.randint(8, 25)

        elif weather == "Rain":

            temperature = random.randint(20, 30)
            humidity = random.randint(75, 100)
            visibility = random.randint(2, 6)
            wind_speed = random.randint(10, 30)

        elif weather == "Fog":

            temperature = random.randint(10, 20)
            humidity = random.randint(85, 100)
            visibility = random.randint(1, 3)
            wind_speed = random.randint(5, 15)

        else:   # Thunderstorm

            temperature = random.randint(18, 28)
            humidity = random.randint(85, 100)
            visibility = random.randint(1, 4)
            wind_speed = random.randint(25, 60)

        return {

            "WeatherCondition": weather,
            "Temperature": temperature,
            "Humidity": humidity,
            "VisibilityKM": visibility,
            "WindSpeedKmph": wind_speed

        }

    # ---------------------------------------

    def generate_delay(self, weather):

        # Weather delay
        min_delay, max_delay = WEATHER_DELAY_RANGES[weather]

        weather_delay = random.randint(min_delay, max_delay)

        # Operational delays

        carrier_delay = (
        random.randint(*CARRIER_DELAY_RANGE)
        if random.random() < CARRIER_DELAY_PROBABILITY
        else 0
        )

        nas_delay = (
        random.randint(*NAS_DELAY_RANGE)
        if random.random() < NAS_DELAY_PROBABILITY
        else 0
        )

        late_aircraft_delay = (
        random.randint(*LATE_AIRCRAFT_DELAY_RANGE)
        if random.random() < LATE_AIRCRAFT_DELAY_PROBABILITY
        else 0
        )

        security_delay = (
        random.randint(*SECURITY_DELAY_RANGE)
        if random.random() < SECURITY_DELAY_PROBABILITY
        else 0
        )

        # Total departure delay

        departure_delay = (

            weather_delay

            + carrier_delay

            + nas_delay

            + late_aircraft_delay

            + security_delay

        )

        # Aircraft may recover some time during flight

        arrival_delay = max(
            0,
            departure_delay + random.randint(-10, 10)
        )

        return {

            "WeatherDelay": weather_delay,

            "CarrierDelay": carrier_delay,

            "NASDelay": nas_delay,

            "LateAircraftDelay": late_aircraft_delay,

            "SecurityDelay": security_delay,

            "DepartureDelayMinutes": departure_delay,

            "ArrivalDelayMinutes": arrival_delay

        }

    # ---------------------------------------

    def generate_passenger(self, aircraft):

        capacity = aircraft["SeatCapacity"]

        passengers = generate_passenger_count(capacity)

        load_factor = generate_load_factor(
            passengers,
            capacity
        )

        average_baggage = random.randint(15, 23)

        baggage_weight = passengers * average_baggage

        if capacity <= 80:

            crew_count = random.randint(4, 5)

        elif capacity <= 200:

            crew_count = random.randint(5, 7)

        elif capacity <= 300:

            crew_count = random.randint(7, 9)

        else:

            crew_count = random.randint(10, 14)

        fuel_consumption = random.randint(

            int(aircraft["FuelCapacityLiters"] * 0.35),

            int(aircraft["FuelCapacityLiters"] * 0.85)

        )

        return {

            "SeatCapacity": capacity,

            "PassengerCount": passengers,

            "LoadFactor": load_factor,

            "CrewCount": crew_count,

            "BaggageWeightKG": baggage_weight,

            "FuelConsumptionLiters": fuel_consumption

        }

    # ---------------------------------------

    def generate_status(self, weather, departure_delay):

        # Small chance of cancellation during severe weather
        if weather == "Thunderstorm" and departure_delay >= 120:

            if random.random() < 0.30:

                return {

                    "FlightStatus": "Cancelled",

                    "CancellationReason": random.choice(
                        CANCELLATION_REASONS
                    )

                }

        if departure_delay <= 15:

            status = "On Time"

        elif departure_delay <= 60:

            status = "Delayed"

        else:

            status = "Heavily Delayed"

        return {

            "FlightStatus": status,

            "CancellationReason": None

        }



    # ---------------------------------------

    def generate_row(self, flight_id):

        # Flight Information
        flight_info, aircraft = self.generate_flight_information(flight_id)

        # Route
        route = self.generate_route()

        # Schedule
        schedule = self.generate_schedule(
            route["DistanceKM"],
            aircraft
        )

        # Weather
        weather = self.generate_weather()

        # Delay
        delay = self.generate_delay(
            weather["WeatherCondition"]
        )

        actual_times = generate_actual_times(
        schedule,
        delay
        )


        # Passenger
        passenger = self.generate_passenger(aircraft)

        # Status
        status = self.generate_status(
            weather["WeatherCondition"],
            delay["DepartureDelayMinutes"]
        )

        # Merge everything
        row = {}

        row.update(flight_info)
        row.update(route)
        row.update(schedule)
        row.update(weather)
        row.update(delay)
        row.update(passenger)
        row.update(status)
        row.update(actual_times)

        return row

    # ---------------------------------------

    def generate_dataset(self):

        self.data = []

        for flight_id in range(1, FLIGHT_ROWS + 1):

            self.data.append(

                self.generate_row(flight_id)

            )

        self.df = pd.DataFrame(self.data)

        return self.df

    # ---------------------------------------

    def save_csv(self):

        os.makedirs("Dataset", exist_ok=True)

        # Generate clean dataset
        df = self.generate_dataset()

        # Create Bronze copy
        bronze_df = df.copy()

        protected_columns = {

            "FlightID",
            "FlightNumber",
            "AircraftID",
            "OriginAirportID",
            "DestinationAirportID"

        }

        for column in bronze_df.columns:

            if column not in protected_columns:

                bronze_df[column] = bronze_df[column].apply(make_bronze)

        bronze_df.to_csv(

            "Dataset/Flights_Raw.csv",

            index=False

        )

        print(f"✅ Flights_Raw.csv created successfully.")
        print(f"Total Records : {len(bronze_df):,}")

        return bronze_df


if __name__ == "__main__":

    generator = FlightGenerator()

    print(generator.save_csv())


