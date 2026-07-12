# ==========================================
# config.py
# Enterprise Airline Bronze Dataset Generator
# ==========================================

import random

# =====================================================
# RANDOM SEED
# =====================================================

RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# =====================================================
# DATASET SIZES
# =====================================================

AIRPORT_ROWS = 150
AIRCRAFT_ROWS = 500
FLIGHT_ROWS = 500_000
WEATHER_ROWS = 100_000
BOOKING_ROWS = 300_000
MAINTENANCE_ROWS = 20_000

# =====================================================
# DATE RANGE
# =====================================================

START_DATE = "2024-01-01"
END_DATE = "2024-12-31"

# =====================================================
# AIRLINES
# =====================================================

AIRLINES = [
    "Air India",
    "IndiGo",
    "Akasa Air",
    "SpiceJet",
    "Air India Express",
    "Alliance Air"
]

# =====================================================
# AIRCRAFT MASTER
# =====================================================

AIRCRAFT_MASTER = [

    {
        "Manufacturer": "Airbus",
        "Model": "A319",
        "SeatCapacity": 144,
        "CruiseSpeed": 828,
        "EngineType": "Turbofan",
        "FuelCapacityLiters": 23860
    },

    {
        "Manufacturer": "Airbus",
        "Model": "A320-200",
        "SeatCapacity": 180,
        "CruiseSpeed": 828,
        "EngineType": "Turbofan",
        "FuelCapacityLiters": 24210
    },

    {
        "Manufacturer": "Airbus",
        "Model": "A320neo",
        "SeatCapacity": 186,
        "CruiseSpeed": 833,
        "EngineType": "Turbofan",
        "FuelCapacityLiters": 24210
    },

    {
        "Manufacturer": "Airbus",
        "Model": "A321neo",
        "SeatCapacity": 220,
        "CruiseSpeed": 833,
        "EngineType": "Turbofan",
        "FuelCapacityLiters": 32000
    },

    {
        "Manufacturer": "Boeing",
        "Model": "737-800",
        "SeatCapacity": 189,
        "CruiseSpeed": 842,
        "EngineType": "Turbofan",
        "FuelCapacityLiters": 26020
    },

    {
        "Manufacturer": "Boeing",
        "Model": "737 MAX 8",
        "SeatCapacity": 210,
        "CruiseSpeed": 839,
        "EngineType": "Turbofan",
        "FuelCapacityLiters": 26020
    },

    {
        "Manufacturer": "Boeing",
        "Model": "777-300ER",
        "SeatCapacity": 396,
        "CruiseSpeed": 905,
        "EngineType": "Turbofan",
        "FuelCapacityLiters": 181280
    },

    {
        "Manufacturer": "Boeing",
        "Model": "787-8",
        "SeatCapacity": 256,
        "CruiseSpeed": 903,
        "EngineType": "Turbofan",
        "FuelCapacityLiters": 126000
    },

    {
        "Manufacturer": "ATR",
        "Model": "ATR 72-600",
        "SeatCapacity": 72,
        "CruiseSpeed": 510,
        "EngineType": "Turboprop",
        "FuelCapacityLiters": 5000
    },

    {
        "Manufacturer": "ATR",
        "Model": "ATR 42-600",
        "SeatCapacity": 50,
        "CruiseSpeed": 556,
        "EngineType": "Turboprop",
        "FuelCapacityLiters": 5000
    }

]

# =====================================================
# AIRPORTS
# =====================================================

# =====================================================
# AIRPORT MASTER
# =====================================================

AIRPORTS = [

    {
        "AirportID": "AP001",
        "Code": "BOM",
        "AirportName": "Chhatrapati Shivaji Maharaj International Airport",
        "City": "Mumbai",
        "State": "Maharashtra",
        "Country": "India",
        "Timezone": "Asia/Kolkata"
    },

    {
        "AirportID": "AP002",
        "Code": "DEL",
        "AirportName": "Indira Gandhi International Airport",
        "City": "New Delhi",
        "State": "Delhi",
        "Country": "India",
        "Timezone": "Asia/Kolkata"
    },

    {
        "AirportID": "AP003",
        "Code": "BLR",
        "AirportName": "Kempegowda International Airport",
        "City": "Bengaluru",
        "State": "Karnataka",
        "Country": "India",
        "Timezone": "Asia/Kolkata"
    },

    {
        "AirportID": "AP004",
        "Code": "HYD",
        "AirportName": "Rajiv Gandhi International Airport",
        "City": "Hyderabad",
        "State": "Telangana",
        "Country": "India",
        "Timezone": "Asia/Kolkata"
    },

    {
        "AirportID": "AP005",
        "Code": "MAA",
        "AirportName": "Chennai International Airport",
        "City": "Chennai",
        "State": "Tamil Nadu",
        "Country": "India",
        "Timezone": "Asia/Kolkata"
    },

    {
        "AirportID": "AP006",
        "Code": "CCU",
        "AirportName": "Netaji Subhas Chandra Bose International Airport",
        "City": "Kolkata",
        "State": "West Bengal",
        "Country": "India",
        "Timezone": "Asia/Kolkata"
    },

    {
        "AirportID": "AP007",
        "Code": "AMD",
        "AirportName": "Sardar Vallabhbhai Patel International Airport",
        "City": "Ahmedabad",
        "State": "Gujarat",
        "Country": "India",
        "Timezone": "Asia/Kolkata"
    },

    {
        "AirportID": "AP008",
        "Code": "PNQ",
        "AirportName": "Pune Airport",
        "City": "Pune",
        "State": "Maharashtra",
        "Country": "India",
        "Timezone": "Asia/Kolkata"
    },

    {
        "AirportID": "AP009",
        "Code": "COK",
        "AirportName": "Cochin International Airport",
        "City": "Kochi",
        "State": "Kerala",
        "Country": "India",
        "Timezone": "Asia/Kolkata"
    },

    {
        "AirportID": "AP010",
        "Code": "GOX",
        "AirportName": "Manohar International Airport",
        "City": "Goa",
        "State": "Goa",
        "Country": "India",
        "Timezone": "Asia/Kolkata"
    }

]

# =====================================================
# WEATHER
# =====================================================

WEATHER_CONDITIONS = [

    "Clear",
    "Cloudy",
    "Rain",
    "Thunderstorm",
    "Fog",
    "Haze",
    "Windy"

]

# =====================================================
# DELAY CONFIGURATION
# =====================================================

# Weather-based delay ranges (minutes)
WEATHER_DELAY_RANGES = {

    "Clear": (0, 5),

    "Cloudy": (0, 10),

    "Rain": (15, 45),

    "Fog": (30, 90),

    "Thunderstorm": (60, 180)

}

# Operational delays (minutes)

CARRIER_DELAY_RANGE = (0, 20)

NAS_DELAY_RANGE = (0, 20)

LATE_AIRCRAFT_DELAY_RANGE = (0, 40)

SECURITY_DELAY_RANGE = (0, 10)

# =====================================================
# DELAY PROBABILITIES
# =====================================================

CARRIER_DELAY_PROBABILITY = 0.30
NAS_DELAY_PROBABILITY = 0.25
LATE_AIRCRAFT_DELAY_PROBABILITY = 0.20
SECURITY_DELAY_PROBABILITY = 0.05

# =====================================================
# TERMINALS
# =====================================================

TERMINALS = [

    "T1",
    "T2",
    "T3"

]

# =====================================================
# GATES
# =====================================================

GATES = [

    f"G{i}" for i in range(1,51)

]

# =====================================================
# CANCELLATION REASONS
# =====================================================

CANCELLATION_REASONS = [

    "Weather",
    "Technical",
    "Crew",
    "ATC",
    "Operational"

]

# =====================================================
# BOOKING
# =====================================================

TICKET_CLASSES = [

    "Economy",
    "Premium Economy",
    "Business"

]

BOOKING_CHANNELS = [

    "Website",
    "Mobile App",
    "Travel Agent"

]

PAYMENT_METHODS = [

    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Wallet"

]

BOOKING_STATUS = [

    "Confirmed",
    "Cancelled",
    "Pending"

]

# =====================================================
# MAINTENANCE
# =====================================================

MAINTENANCE_TYPES = [

    "Routine",
    "Engine Check",
    "Landing Gear",
    "Avionics",
    "Emergency Repair"

]

MAINTENANCE_STATUS = [

    "Scheduled",
    "In Progress",
    "Completed"

]

# =====================================================
# ENGINE TYPES
# =====================================================

ENGINE_TYPES = [

    "Turbofan",
    "Turbojet",
    "Turboprop"

]

# =====================================================
# BRONZE DATA QUALITY SETTINGS
# =====================================================

MISSING_VALUE_RATE = 0.05
DUPLICATE_RATE = 0.02
INVALID_VALUE_RATE = 0.01
MIXED_CASE_RATE = 0.05
EXTRA_SPACE_RATE = 0.03
MIXED_DATE_FORMAT_RATE = 0.05