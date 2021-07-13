import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = (int(row[5])-32)*5/9
        low = (int(row[6])-32)*5/9
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=1, linewidth=1)
ax.plot(dates, lows, c='blue', alpha=1, linewidth=1)
plt.fill_between(dates, highs, lows, facecolors='grey', alpha=0.3)

plt.title("Daily high and low temperatures, 2018", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
