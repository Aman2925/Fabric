# =====================================================
# aircraft.py
# Enterprise Airline Bronze Dataset Generator
# =====================================================

import random
import pandas as pd
import os 

from config import *
from utils import *


class AircraftGenerator:

    def __init__(self):

        self.aircraft_master = AIRCRAFT_MASTER
        self.airports = AIRPORTS

        self.data = []

    def generate_aircraft(self, aircraft_id):

        aircraft = random.choice(self.aircraft_master)

        base_airport = random.choice(self.airports)

        age = random.randint(1, 20)

        last_maintenance = random_date()

        next_maintenance = last_maintenance + timedelta(days=random.randint(30, 180))

        status = random.choices(

            population=[
                "Active",
                "Maintenance",
                "Grounded"
            ],

            weights=[
                90,
                8,
                2
            ]

        )[0]

        row = {

            "AircraftID": f"AC{aircraft_id:03}",

            "TailNumber": generate_tail_number(),

            "Manufacturer": aircraft["Manufacturer"],

            "Model": aircraft["Model"],

            "SeatCapacity": aircraft["SeatCapacity"],

            "CruiseSpeed": aircraft["CruiseSpeed"],

            "EngineType": aircraft["EngineType"],

            "FuelCapacityLiters": aircraft["FuelCapacityLiters"],

            "AircraftAge": age,

            "BaseAirportID": base_airport["AirportID"],

            "BaseAirportCode": base_airport["Code"],

            "BaseAirportCity": base_airport["City"],

            "BaseAirportName": base_airport["AirportName"],

            "Status": status,

            "LastMaintenanceDate": last_maintenance,

            "NextMaintenanceDate": next_maintenance,

            "RecordCreatedAt": generate_record_timestamp()

        }

        return row
    
    def introduce_errors(self, row):

        protected_columns = {

            "AircraftID",
            "BaseAirportID"

        }

        bronze_row = {}

        for key, value in row.items():

            if key in protected_columns:

                bronze_row[key] = value

            else:

                bronze_row[key] = make_bronze(value)

        return bronze_row
    
    def generate_dataset(self):

        self.data = []

        for aircraft_id in range(1, AIRCRAFT_ROWS + 1):

            clean_row = self.generate_aircraft(aircraft_id)

            self.data.append(clean_row)

        self.df = pd.DataFrame(self.data)

        return self.df
    

    def save_csv(self):

        os.makedirs("Dataset", exist_ok=True)

        # Generate clean dataset
        df = self.generate_dataset()

        # Copy it for Bronze conversion
        bronze_df = df.copy()

        protected_columns = {
            "AircraftID",
            "BaseAirportID"
        }

        for column in bronze_df.columns:

            if column not in protected_columns:

                bronze_df[column] = bronze_df[column].apply(make_bronze)

        bronze_df.to_csv(
            "Dataset/Aircraft_Raw.csv",
            index=False
        )

        print(f"✅ {len(bronze_df)} Aircraft Records Generated Successfully.")

        return bronze_df

 

if __name__ == "__main__":

    generator = AircraftGenerator()

    generator.save_csv()