import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_FILE = BASE_DIR / "data" / "raw" / "airline_route_profitability.csv"
LOOKUP_FILE = BASE_DIR / "data" / "lookup" / "airport_lookup.csv"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
OUTPUT_FILE = PROCESSED_DIR / "airline_cleaned.csv"

print("=" * 70)
print("AIRLINE DATA CLEANING & VALIDATION PIPELINE STARTED")
print("=" * 70)

df = pd.read_csv(RAW_FILE)

print(f"Original rows    : {df.shape[0]}")
print(f"Original columns : {df.shape[1]}")

duplicate_count = df.duplicated().sum()
print(f"Duplicate rows   : {duplicate_count}")

df["Flight_Date"] = pd.to_datetime(
    df["Flight_Date"],
    format="%Y-%m-%d",
    errors="coerce"
)
print(f"Invalid dates    : {df['Flight_Date'].isna().sum()}")

columns_to_fill = ["Ancillary_Revenue", "Catering_Cost", "Handling_Cost"]

for col in columns_to_fill:
    if col in df.columns:
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)

df["Year"] = df["Flight_Date"].dt.year
df["Quarter"] = df["Flight_Date"].dt.quarter
df["Month_Number"] = df["Flight_Date"].dt.month
df["Month"] = df["Flight_Date"].dt.month_name()
df["Day"] = df["Flight_Date"].dt.day
df["Day_Name"] = df["Flight_Date"].dt.day_name()

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_FILE, index=False)
print(f"\nCleaned dataset saved successfully to: {OUTPUT_FILE}")

total_flights = len(df)
total_passengers = df["Passengers"].sum()
total_revenue = df["Total_Revenue"].sum()
total_cost = df["Total_Cost"].sum()
total_profit = df["Profit"].sum()
profit_margin_pct = (total_profit / total_revenue) * 100

profitable_flights = (df["Profit"] > 0).sum()
loss_flights = (df["Profit"] < 0).sum()

print("\n" + "=" * 70)
print("VALIDATION SUMMARY (TARGET vs CALCULATED)")
print("=" * 70)
print(f"Total Flights          : {total_flights:12,d} | Target: 7,974")
print(f"Total Passengers       : {total_passengers:12,d}")
print(f"Total Revenue          : ${total_revenue:14,.2f}")
print(f"Total Cost             : ${total_cost:14,.2f}")
print(f"Total Profit           : ${total_profit:14,.2f}")
print(f"Profit Margin %        : {profit_margin_pct:12.2f}%")
print(f"Profitable Flights     : {profitable_flights:12,d}")
print(f"Loss-Making Flights    : {loss_flights:12,d}")
print("=" * 70)
