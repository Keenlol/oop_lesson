import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print all cities in Italy
cities_temp = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        cities_temp.append(city['city'])
print("All the cities in", my_country, ":")
print(cities_temp)
print()

# Print the average temperature for all the cities in Italy
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The average temperature of all the cities in", my_country, ":")
print(sum(temps)/len(temps))
print()

# Print the max temperature for all the cities in Italy
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The max temperature of all the cities in", my_country, ":")
print(max(temps))
print()

# Print the min temperature for all the cities in Italy
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The min temperature of all the cities in", my_country, ":")
print(min(temps))
print()

# Let's write code to
# - print the average temperature for all the cities in Italy
# - print the average temperature for all the cities in Sweden
# - print the min temperature for all the cities in Italy
# - print the max temperature for all the cities in Sweden
