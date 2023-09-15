import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("climate.csv")

df1 = df.head(10)
print(df1)

years = []
co2 = []
temp = []

for i in range(len(df)):
    if df['Years']:
        years.append(df['Years'])
    elif df['CO2']:
        co2.append(df['CO2'])
    else:
        temp.append(df['Temperature'])


plt.subplot(2, 1, 1)
plt.plot(years, co2, 'bo')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_2.png")

