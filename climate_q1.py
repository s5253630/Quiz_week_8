import matplotlib.pyplot as plt
import sqlite3

con = sqlite3.connect('climate.db')
cursor = con.cursor()

cursor.execute("select name from sqlite_master where type='table';")
tables = cursor.fetchall()

for i in tables:
    table_name = i[0]
    cursor.execute(f"select * from {table_name}")
    col = sqlite3.Row(cursor,(1,)).keys() # Print the row
    print(col)
res = cursor.execute("select * from ClimateData;")
for i in res:
    print(i)

years = list(con.execute("select year from ClimateData;"))
co2 = list(con.execute("select co2 from ClimateData;"))
temp = list(con.execute("select temperature from ClimateData;"))

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'ro-')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'b*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_1.png")
