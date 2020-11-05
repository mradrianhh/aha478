import numpy as np
import matplotlib.pyplot as plt

# Use recursion.
def fortune(year, interest_rate, yearly_consumption):
    if year == 0:
        return 100000
    else:
        return fortune(year-1, interest_rate, yearly_consumption) + interest_rate/100*fortune(year-1, interest_rate, yearly_consumption) - yearly_consumption

# Use recursion.
def yearly_consumption(year, inflation):
    if year == 0:
        return 1000
    else:
        return yearly_consumption(year-1, inflation) + inflation/100*yearly_consumption(year-1, inflation)

years = np.linspace(1, 20, 20)
inflations = np.linspace(1, 7, 5)

fortunes = []
for year in years:
    fortunes.append(fortune(year, 0.023, 1000))

plt.plot(years, fortunes, label = "No inflation")

for inflation in inflations:
    fortunes = [] # Reset fortunes for each year.
    for year in years:
        fortunes.append(fortune(year, 0.023, yearly_consumption(year, inflation)))
    plt.plot(years, fortunes, label = f"inflation: {inflation}")

plt.legend()
plt.show()