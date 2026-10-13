import pandas as pd
import numpy as np

# Read the CSV
data = pd.read_csv("day02_usage.csv")

# A — Build the table
apps = data[["Chat", "Video", "Study", "Games"]].to_numpy()

print("Shape:", apps.shape)


# B — The direction dial

print("\nTotals per app:")
print(apps.sum(axis=0))

print("Totals per day:")
print(apps.sum(axis=1))

print("\nMean per app:")
print(apps.mean(axis=0))

print("Mean per day:")
print(apps.mean(axis=1))

print("\nMaximum per app:")
print(apps.max(axis=0))

print("Maximum per day:")
print(apps.max(axis=1))

print("\nMinimum per app:")
print(apps.min(axis=0))

print("Minimum per day:")
print(apps.min(axis=1))


# C — Find the winning app for each day

app_names = np.array(["Chat", "Video", "Study", "Games"])

winner_position = apps.argmax(axis=1)

winners = app_names[winner_position]

print("\nWinner for each day:")
print(winners)

winner_names, winner_counts = np.unique(winners, return_counts=True)

print("\nNumber of days each app won:")

for name, count in zip(winner_names, winner_counts):
    print(name, ":", count)


# D — Broadcasting

# Total minutes for each day
day_totals = apps.sum(axis=1)

# Convert totals into a column
day_totals = day_totals[:, np.newaxis]

# Percentage of each app for every day
percentages = (apps / day_totals) * 100

print("\nFirst day's percentages:")
print(percentages[0])

print("First row total:", percentages[0].sum())


# Scale every app against its own maximum

app_maximums = apps.max(axis=0)

scaled = apps / app_maximums

print("\nScaled first row:")
print(scaled[0])


# E — Weekend and weekday analysis

# Assuming the CSV has a Date column
dates = pd.to_datetime(data["Date"])

weekend = dates.dt.dayofweek >= 5
weekday = dates.dt.dayofweek < 5

weekend_average = apps[weekend].mean(axis=0)
weekday_average = apps[weekday].mean(axis=0)

print("\nWeekend averages:")
print(weekend_average)

print("\nWeekday averages:")
print(weekday_average)


# Busiest day of the month

busiest_position = day_totals.argmax()

print("\nBusiest day:")
print(data["Date"].iloc[busiest_position])

print("Minutes:", day_totals[busiest_position, 0])