import sqlite3

connection = sqlite3.connect("census.db", timeout=10)

cursor = connection.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS density( province_or_teritory TEXT ,population INTEGER,land_area REAL)")

# cursor.execute("INSERT INTO main.density VALUES('Newfoundland and Labrador', 512930 ,370501.69)")
# cursor.execute("INSERT INTO main.density VALUES('Prince Edward Island', 135294 ,5684.39)")
# cursor.execute("INSERT INTO main.density VALUES('Nova Scotia', 908007 , 52917.43)")
# cursor.execute("INSERT INTO main.density VALUES('New Brunswick', 729498 ,71355.67)")
# cursor.execute("INSERT INTO main.density VALUES('Quebec', 7237479,1357743.08)")
# cursor.execute("INSERT INTO main.density VALUES('Ontario', 11410046 ,907655.59)")
# cursor.execute("INSERT INTO main.density VALUES('Manitoba', 1119583,551937.87)")
# cursor.execute("INSERT INTO main.density VALUES('Saskatchewan', 978933 ,586561.35)")
# cursor.execute("INSERT INTO main.density VALUES('Alberta', 2974807 ,639987.12)")
# cursor.execute("INSERT INTO main.density VALUES('British Columbia', 3907738,926492.48)")
# cursor.execute("INSERT INTO main.density VALUES('Yukon Territory',  28674  ,474706.97)")
# cursor.execute("INSERT INTO main.density VALUES('Northwest Territories', 37360 ,1141108.37)")
# cursor.execute("INSERT INTO main.density VALUES('Nunavut', 26745 ,1925460.18)")

#connection.commit()

#cursor.execute("SELECT * FROM density")                        #ბეჭდავს ყველაფერს
#cursor.execute("SELECT density.population FROM density")        #მხოლოდ მოსახლეობა
#cursor.execute("SELECT density.province_or_teritory FROM density WHERE density.population < 1000000")   #1 მილიონზე ნაკლები ადამიანი
#cursor.execute("SELECT density.province_or_teritory FROM density WHERE density.population < 1000000 OR density.population > 5000000") #1 მილიონზე ნაკლები ან 5 მილიონზე მეტი
#cursor.execute("SELECT density.province_or_teritory FROM density WHERE density.province_or_teritory NOT IN (SELECT density.province_or_teritory FROM density WHERE density.population < 1000000 OR density.population > 5000000)") #ზედა ოღოდ პირიქით
#cursor.execute("SELECT density.population FROM density WHERE density.land_area > 200000")
#cursor.execute("SELECT density.province_or_teritory, (density.population/density.land_area) AS სიმჭირდოვე FROM density ")

for i in cursor:
    print(i)





















