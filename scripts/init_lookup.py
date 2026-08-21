import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(r"C:\Users\91638\Desktop\AIRLINE_DATA_ANALYTICS")
RAW_DIR = BASE_DIR / "data" / "raw"
LOOKUP_DIR = BASE_DIR / "data" / "lookup"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

RAW_DIR.mkdir(parents=True, exist_ok=True)
LOOKUP_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# 1. Save airport lookup CSV
airport_lookup_csv = """Airport_Code,Airport_Name,Airport_City,Country,Latitude,Longitude
DXB,Dubai International Airport,Dubai,United Arab Emirates,25.2532,55.3657
AMM,Queen Alia International Airport,Amman,Jordan,31.7226,35.9932
BAH,Bahrain International Airport,Manama,Bahrain,26.2708,50.6336
BKK,Suvarnabhumi Airport,Bangkok,Thailand,13.69,100.7501
BLR,Kempegowda International Airport,Bengaluru,India,13.1986,77.7066
BOM,Chhatrapati Shivaji Maharaj International Airport,Mumbai,India,19.0896,72.8656
CAI,Cairo International Airport,Cairo,Egypt,30.1219,31.4056
CDG,Charles de Gaulle Airport,Paris,France,49.0097,2.5479
CMB,Bandaranaike International Airport,Colombo,Sri Lanka,7.1808,79.8841
DEL,Indira Gandhi International Airport,Delhi,India,28.5562,77.1
DOH,Hamad International Airport,Doha,Qatar,25.2731,51.6081
FRA,Frankfurt Airport,Frankfurt,Germany,50.0379,8.5622
HKG,Hong Kong International Airport,Hong Kong,Hong Kong,22.308,113.9185
HYD,Rajiv Gandhi International Airport,Hyderabad,India,17.2403,78.4294
IST,Istanbul Airport,Istanbul,Türkiye,41.2753,28.7519
JED,King Abdulaziz International Airport,Jeddah,Saudi Arabia,21.6702,39.1525
JFK,John F. Kennedy International Airport,New York,United States,40.6413,-73.7781
KHI,Jinnah International Airport,Karachi,Pakistan,24.9065,67.1608
KUL,Kuala Lumpur International Airport,Kuala Lumpur,Malaysia,2.7456,101.7072
KWI,Kuwait International Airport,Kuwait City,Kuwait,29.2266,47.9689
LAX,Los Angeles International Airport,Los Angeles,United States,33.9416,-118.4085
LHE,Allama Iqbal International Airport,Lahore,Pakistan,31.5216,74.4036
LHR,Heathrow Airport,London,United Kingdom,51.47,-0.4543
MAA,Chennai International Airport,Chennai,India,12.9941,80.1709
MCT,Muscat International Airport,Muscat,Oman,23.5933,58.2844
MEL,Melbourne Airport,Melbourne,Australia,-37.669,144.841
ORD,O'Hare International Airport,Chicago,United States,41.9742,-87.9073
RUH,King Khalid International Airport,Riyadh,Saudi Arabia,24.9576,46.6988
SFO,San Francisco International Airport,San Francisco,United States,37.6213,-122.379
SIN,Singapore Changi Airport,Singapore,Singapore,1.3644,103.9915
SYD,Sydney Kingsford Smith Airport,Sydney,Australia,-33.9399,151.1753"""

with open(LOOKUP_DIR / "airport_lookup.csv", "w", encoding="utf-8") as f:
    f.write(airport_lookup_csv)

with open(RAW_DIR / "airport_lookup.csv", "w", encoding="utf-8") as f:
    f.write(airport_lookup_csv)

print("airport_lookup.csv written successfully to lookup and raw folders.")
