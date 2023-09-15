import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("climate.csv")

df1 = df.head(10)
print(df1)

years = list(df['Year'])
co2 = list(df['CO2'])
temp = list(df['Temperature'])


plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, '*--')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_2.png")

