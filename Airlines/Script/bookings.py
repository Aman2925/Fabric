# =====================================================
# bookings.py
# Enterprise Airline Bronze Dataset Generator
# =====================================================

from flights import FlightGenerator
import random
import pandas as pd
import os

from config import *
from utils import *


class BookingGenerator:

    def __init__(self):

        flight_generator = FlightGenerator()

        self.flight_data = flight_generator.generate_dataset().to_dict("records")

        self.data = []

    # ---------------------------------------

    def generate_booking(self, booking_id):

        flight = random.choice(self.flight_data)

        travel_date = flight["FlightDate"]

        days_before = random.choices(
            population=[
                random.randint(1, 7),
                random.randint(8, 30),
                random.randint(31, 90),
                random.randint(91, 180)
            ],
            weights=[25, 40, 25, 10]
        )[0]

        booking_date = travel_date - timedelta(days=days_before)

        ticket_class = random.choices(

            population=[
                "Economy",
                "Premium Economy",
                "Business"
            ],

            weights=[
                75,
                15,
                10
            ]

        )[0]

        passenger_type = random.choices(

            population=[
                "Adult",
                "Child",
                "Infant"
            ],

            weights=[
                88,
                9,
                3
            ]

        )[0]

        booking_channel = random.choices(

            population=BOOKING_CHANNELS,

            weights=[
                45,
                40,
                15
            ]

        )[0]

        payment_method = random.choices(

            population=PAYMENT_METHODS,

            weights=[
                40,
                25,
                20,
                10,
                5
            ]

        )[0]

        booking_status = random.choices(

            population=BOOKING_STATUS,

            weights=[
                90,
                7,
                3
            ]

        )[0]

            # -------------------------------
    # Base Fare
    # -------------------------------

        if ticket_class == "Economy":

            base_fare = random.randint(2500,8000)

        elif ticket_class == "Premium Economy":

            base_fare = random.randint(6000,15000)

        else:

            base_fare = random.randint(15000,45000)

        tax_amount = round(base_fare * 0.18)

        discount = random.choice([0,500,1000,1500])

        total_amount = base_fare + tax_amount - discount

        seat_row = random.randint(1,45)

        seat_letter = random.choice(

            ["A","B","C","D","E","F"]

        )

        seat_number = f"{seat_row}{seat_letter}"

        meal = random.choice(

            [

                "Veg",

                "Non-Veg",

                "Jain",

                "Vegan",

                "None"

            ]

        )

        baggage = random.choice(

            [0,5,10,15,20]

        )

        loyalty = random.choice(

            [

                "Yes",

                "No"

            ]

        )

        return {

        "BookingID": f"BK{booking_id:07d}",

        "FlightID": flight["FlightID"],

        "BookingDate": booking_date,

        "TravelDate": travel_date,

        "TicketClass": ticket_class,

        "PassengerType": passenger_type,

        "BookingChannel": booking_channel,

        "PaymentMethod": payment_method,

        "BaseFare": base_fare,

        "TaxAmount": tax_amount,

        "DiscountAmount": discount,

        "TotalAmount": total_amount,

        "SeatNumber": seat_number,

        "MealPreference": meal,

        "ExtraBaggageKG": baggage,

        "LoyaltyMember": loyalty,

        "BookingStatus": booking_status,

        "RecordCreatedAt": generate_record_timestamp()

    }
    # ---------------------------------------

    def generate_dataset(self):

        self.data = []

        for booking_id in range(1, BOOKING_ROWS + 1):

            self.data.append(

                self.generate_booking(booking_id)

            )

        self.df = pd.DataFrame(self.data)

        return self.df

    # ---------------------------------------

    def save_csv(self):

        os.makedirs("Dataset", exist_ok=True)

        df = self.generate_dataset()

        bronze_df = df.copy()

        protected_columns = {

            "BookingID",
            "FlightID"

        }

        for column in bronze_df.columns:

            if column not in protected_columns:

                bronze_df[column] = bronze_df[column].apply(make_bronze)

        bronze_df.to_csv(

            "Dataset/Bookings_Raw.csv",

            index=False

        )

        print("✅ Bookings_Raw.csv created successfully.")
        print(f"Total Records : {len(bronze_df):,}")

        print(bronze_df)


if __name__ == "__main__":

    generator = BookingGenerator()

    print(generator.save_csv())