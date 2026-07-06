# =====================================================
# weather.py
# Enterprise Airline Bronze Dataset Generator
# =====================================================

import random
import pandas as pd
import os

from config import *
from utils import *


class WeatherGenerator:

    def __init__(self):

        self.airports = AIRPORTS

        self.data = []

    # ---------------------------------------

    def generate_weather(self, weather_id):

        airport = random.choice(self.airports)

        observation_date = random_date()

        weather = random_weather()

        # ----------------------------------
        # Clear
        # ----------------------------------

        if weather == "Clear":

            temperature = random.randint(28,40)
            humidity = random.randint(35,60)
            visibility = random.randint(8,10)
            wind_speed = random.randint(5,20)
            pressure = random.randint(1010,1025)
            rainfall = 0
            severity = "Low"

        # ----------------------------------
        # Cloudy
        # ----------------------------------

        elif weather == "Cloudy":

            temperature = random.randint(22,34)
            humidity = random.randint(55,80)
            visibility = random.randint(6,9)
            wind_speed = random.randint(8,25)
            pressure = random.randint(1008,1018)
            rainfall = random.randint(0,3)
            severity = "Low"

        # ----------------------------------
        # Rain
        # ----------------------------------

        elif weather == "Rain":

            temperature = random.randint(20,30)
            humidity = random.randint(75,100)
            visibility = random.randint(2,6)
            wind_speed = random.randint(10,30)
            pressure = random.randint(995,1008)
            rainfall = random.randint(5,50)
            severity = "Moderate"

        # ----------------------------------
        # Fog
        # ----------------------------------

        elif weather == "Fog":

            temperature = random.randint(10,20)
            humidity = random.randint(85,100)
            visibility = random.randint(1,3)
            wind_speed = random.randint(5,15)
            pressure = random.randint(1005,1018)
            rainfall = 0
            severity = "Moderate"

        # ----------------------------------
        # Thunderstorm
        # ----------------------------------

        else:

            temperature = random.randint(18,28)
            humidity = random.randint(85,100)
            visibility = random.randint(1,4)
            wind_speed = random.randint(25,60)
            pressure = random.randint(980,1000)
            rainfall = random.randint(20,120)
            severity = "High"

        return {

            "WeatherID": f"WTH{weather_id:06}",

            "AirportID": airport["AirportID"],

            "AirportCode": airport["Code"],

            "AirportName": airport["AirportName"],

            "City": airport["City"],

            "ObservationDate": observation_date,

            "ObservationTime": random_time(),

            "WeatherCondition": weather,

            "Temperature": temperature,

            "Humidity": humidity,

            "VisibilityKM": visibility,

            "WindSpeedKmph": wind_speed,

            "PressurehPa": pressure,

            "RainfallMM": rainfall,

            "WeatherSeverity": severity,

            "RecordCreatedAt": generate_record_timestamp()

        }

    # ---------------------------------------

    def generate_dataset(self):

        self.data = []

        for weather_id in range(1, WEATHER_ROWS + 1):

            self.data.append(

                self.generate_weather(weather_id)

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

            "WeatherID",
            "AirportID"

        }

        for column in bronze_df.columns:

            if column not in protected_columns:

                bronze_df[column] = bronze_df[column].apply(make_bronze)

        bronze_df.to_csv(

            "Dataset/Weather_Raw.csv",

            index=False

        )

        print("✅ Weather_Raw.csv created successfully.")
        print(f"Total Records : {len(bronze_df):,}")

        return bronze_df


if __name__ == "__main__":

    generator = WeatherGenerator()

    print(generator.save_csv())