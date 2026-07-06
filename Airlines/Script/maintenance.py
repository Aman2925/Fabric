# =====================================================
# maintenance.py
# =====================================================

from aircrafts import AircraftGenerator
import random
import pandas as pd
import os

from config import *
from utils import *


class MaintenanceGenerator:

    def __init__(self):

        self.aircraft_data = pd.read_csv(
            "Dataset/Aircraft_Raw.csv"
        ).to_dict("records")

        self.data = []


    def generate_maintenance(self, maintenance_id):

        aircraft = random.choice(self.aircraft_data)

        maintenance_type = random.choices(

            population=MAINTENANCE_TYPES,

            weights=[60,15,10,10,5]

        )[0]

        status = random.choices(

            population=MAINTENANCE_STATUS,

            weights=[85,10,5]

        )[0]

        start_date = random_date()

        if maintenance_type == "Routine":

            duration = random.randint(2,8)
            cost = random.randint(10000,50000)
            parts = random.randint(0,2)

        elif maintenance_type == "Engine Check":

            duration = random.randint(8,24)
            cost = random.randint(100000,500000)
            parts = random.randint(2,10)

        elif maintenance_type == "Landing Gear":

            duration = random.randint(10,30)
            cost = random.randint(200000,800000)
            parts = random.randint(1,6)

        elif maintenance_type == "Avionics":

            duration = random.randint(4,16)
            cost = random.randint(50000,300000)
            parts = random.randint(1,5)

        else:

            duration = random.randint(12,72)
            cost = random.randint(500000,2000000)
            parts = random.randint(5,20)

        end_date = start_date + timedelta(hours=duration)

        next_due = end_date + timedelta(days=random.randint(30,180))

        return {

            "MaintenanceID": f"MT{maintenance_id:06}",

            "AircraftID": aircraft["AircraftID"],

            "TailNumber": aircraft["TailNumber"],

            "MaintenanceType": maintenance_type,

            "MaintenanceStatus": status,

            "MaintenanceStartDate": start_date,

            "MaintenanceEndDate": end_date,

            "DurationHours": duration,

            "EngineerID": f"ENG{random.randint(1,250):04}",

            "MaintenanceCost": cost,

            "PartsReplaced": parts,

            "NextMaintenanceDue": next_due,

            "Remarks": random.choice([
                "Routine Inspection",
                "Engine Serviced",
                "Landing Gear Replaced",
                "Software Updated",
                "Emergency Repair Completed"
            ]),

            "RecordCreatedAt": generate_record_timestamp()

        }
    

    def generate_dataset(self):

        self.data = []

        for maintenance_id in range(1, MAINTENANCE_ROWS + 1):

            self.data.append(

                self.generate_maintenance(maintenance_id)

            )

        self.df = pd.DataFrame(self.data)

        return self.df
    

    def save_csv(self):

        os.makedirs("Dataset", exist_ok=True)

        df = self.generate_dataset()

        bronze_df = df.copy()

        protected_columns = {

            "MaintenanceID",
            "AircraftID"

        }

        for column in bronze_df.columns:

            if column not in protected_columns:

                bronze_df[column] = bronze_df[column].apply(make_bronze)

        bronze_df.to_csv(

            "Dataset/Maintenance_Raw.csv",

            index=False

        )

        print("✅ Maintenance_Raw.csv created successfully.")
        print(f"Total Records : {len(bronze_df):,}")
        print(bronze_df)


if __name__ == "__main__":

    generator = MaintenanceGenerator()

    generator.save_csv()