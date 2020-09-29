# Temporary code provided in TC1004B.201
import csv
population_2010 = []
value_errors = ['--','NA']
country_exceptions = ['North America', 'Eurasia', 'Middle East', 'Europe', 'World', 'Country', 'Asia & Oceania', 'Africa', 'Central & South America']
with open("TextFiles/populationbycountry19802010millions.csv") as csvFile:
    reader = csv.reader(csvFile)

    for row in reader:
        if row[-1] not in value_errors and row[0] not in country_exceptions:
            population_2010.append([float(row[-1])], row[0])

population_2010.sort(reverse=True)
print(population_2010[:5])