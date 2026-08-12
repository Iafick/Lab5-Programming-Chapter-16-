"""
Program Name: Ohio Unemployment Data Plot
Author: Imran Afick
Purpose: Read Ohio unemployment data from a CSV file and create
         a time-series line plot using matplotlib.
Starter Code: None. Created for Lab 16, Option 1.
Date: August 11, 2026
"""

import matplotlib.pyplot as plt
import csv
from datetime import datetime

dates = []
unemployment_rates = []

try:
    with open("OHUR.csv", "r") as file:
        reader = csv.reader(file)

        for row_number, row in enumerate(reader):
            if row_number == 0:
                continue

            try:
                date = datetime.strptime(row[0], "%Y-%m-%d")
                unemployment_rate = float(row[1])

                dates.append(date)
                unemployment_rates.append(unemployment_rate)


            except (ValueError, IndexError):
                continue

except FileNotFoundError:
    print("Error: OHUR.csv was not found.")


plt.figure(figsize=(12, 6))
plt.plot(dates, unemployment_rates)

plt.title("Ohio Unemployment (by Month): 1976 - 2022")
plt.xlabel("Date")
plt.ylabel("Unemp Rate")

plt.grid(True)
plt.tight_layout()

plt.savefig("ohio_unemployment.png")
plt.close()
