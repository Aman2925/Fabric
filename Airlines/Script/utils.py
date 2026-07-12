# =====================================================
# utils.py
# Enterprise Airline Bronze Dataset Generator
# =====================================================

import random
import string
from datetime import datetime, timedelta
import pandas as pd
import os

from config import *

# =====================================================
# RANDOM DATE
# =====================================================

def random_date():

    start = datetime.strptime(START_DATE, "%Y-%m-%d")
    end = datetime.strptime(END_DATE, "%Y-%m-%d")

    days = (end - start).days

    return start + timedelta(days=random.randint(0, days))

# =====================================================
# RANDOM TIME
# =====================================================

def random_time():

    hour = random.randint(0, 23)
    minute = random.choice([0,5,10,15,20,25,30,35,40,45,50,55])

    return f"{hour:02}:{minute:02}"

# =====================================================
# DEPARTURE TIME
# =====================================================

def generate_departure_time():

    """
    Airlines don't schedule flights uniformly.
    Morning and evening are busier.
    """

    hour = random.choices(
        population=[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
        weights=[12,12,12,10,9,8,7,5,5,5,6,8,10,12,12,10,6,4,2]
    )[0]

    minute = random.choice([0,5,10,15,20,25,30,35,40,45,50,55])

    return hour, minute

# =====================================================
# RANDOM FLIGHT NUMBER
# =====================================================

def generate_flight_number():

    prefix = random.choice([
        "AI",
        "6E",
        "SG",
        "QP",
        "IX",
        "9I"
    ])

    number = random.randint(100,9999)

    return f"{prefix}{number}"

# =====================================================
# AIRCRAFT ID
# =====================================================

def generate_aircraft_id():

    return f"AC{random.randint(1,AIRCRAFT_ROWS):03}"

# =====================================================
# TAIL NUMBER
# =====================================================

def generate_tail_number():

    letters = ''.join(random.choices(string.ascii_uppercase,k=2))
    digits = random.randint(100,999)

    return f"VT-{letters}{digits}"

# =====================================================
# GATE
# =====================================================

def random_gate():

    return random.choice(GATES)

# =====================================================
# TERMINAL
# =====================================================

def random_terminal():

    return random.choice(TERMINALS)

# =====================================================
# RANDOM WEATHER
# =====================================================

# =====================================================
# RANDOM WEATHER
# =====================================================

def random_weather():

    return random.choices(

        population=[
            "Clear",
            "Cloudy",
            "Rain",
            "Fog",
            "Thunderstorm"
        ],

        weights=[
            55,
            20,
            15,
            5,
            5
        ]

    )[0]

# =====================================================
# DISTANCE
# =====================================================

def random_distance():

    return random.randint(350,2500)

# =====================================================
# TAXI OUT
# =====================================================

def generate_taxi_out():

    return random.randint(8,35)

# =====================================================
# TAXI IN
# =====================================================

def generate_taxi_in():

    return random.randint(5,20)

# =====================================================
# TEMPERATURE
# =====================================================

def random_temperature():

    return random.randint(15,42)

# =====================================================
# HUMIDITY
# =====================================================

def random_humidity():

    return random.randint(35,95)

# =====================================================
# VISIBILITY
# =====================================================

def random_visibility():

    return random.randint(1,10)

# =====================================================
# WIND SPEED
# =====================================================

def random_wind_speed():

    return random.randint(5,60)

# =====================================================
# PASSENGERS
# =====================================================

def generate_passenger_count(capacity):

    return random.randint(int(capacity*0.55),capacity)

# =====================================================
# LOAD FACTOR
# =====================================================

def generate_load_factor(passengers,capacity):

    return round(passengers/capacity,2)

# =====================================================
# BAGGAGE
# =====================================================

def generate_baggage_weight():

    return random.randint(500,4500)

# =====================================================
# FUEL
# =====================================================

def generate_fuel_consumption():

    return random.randint(1800,9000)

# =====================================================
# CREW
# =====================================================

def generate_crew_count():

    return random.randint(4,12)

# =====================================================
# RECORD TIMESTAMP
# =====================================================

def generate_record_timestamp():

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# =====================================================
# BRONZE DATA QUALITY FUNCTIONS
# =====================================================

def random_case(text):

    options = [
        text,
        text.upper(),
        text.lower(),
        text.title()
    ]

    return random.choice(options)

# -----------------------------------------------------

def add_spaces(text):

    options = [

        text,

        " " + text,

        text + " ",

        " " + text + " "

    ]

    return random.choice(options)

# -----------------------------------------------------

def random_missing():

    return random.choice([

        None,
        "",
        " ",
        "N/A",
        "Unknown"

    ])

# -----------------------------------------------------

def random_date_format(dt):

    formats = [

        "%Y-%m-%d",
        "%d/%m/%Y",
        "%b %d, %Y",
        "%d-%m-%Y"

    ]

    return dt.strftime(random.choice(formats))

# -----------------------------------------------------

def introduce_text_errors(value):

    """
    Introduce messy text
    """

    if random.random() < EXTRA_SPACE_RATE:
        value = add_spaces(value)

    if random.random() < MIXED_CASE_RATE:
        value = random_case(value)

    if random.random() < MISSING_VALUE_RATE:
        value = random_missing()

    return value

# -----------------------------------------------------

def introduce_numeric_errors(value):

    if random.random() < INVALID_VALUE_RATE:

        return random.choice([
            -abs(value),
            value * 10,
            None
        ])

    return value

# -----------------------------------------------------

def random_null_date():

    return random.choice([
        None,
        "",
        " ",
        "N/A"
    ])

# -----------------------------------------------------

def make_bronze(value):

    if pd.isna(value):
        return None

    if isinstance(value, str):
        return introduce_text_errors(value)

    if isinstance(value, (int, float)):
        return introduce_numeric_errors(value)

    if isinstance(value, datetime):
        return random_date_format(value)

    return value

def generate_actual_times(schedule, delay):

    return {

        "ActualDeparture":
            schedule["ScheduledDeparture"] + timedelta(
                minutes=delay["DepartureDelayMinutes"]
            ),

        "ActualArrival":
            schedule["ScheduledArrival"] + timedelta(
                minutes=delay["ArrivalDelayMinutes"]
            )

    }