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

# Get average, min or max temperature of the give _country
def temperature(_country, _option):
    temps = []
    for city in cities:
        if city['country'] == _country:
            temps.append(float(city['temperature']))
    
    if _option == "avg":
        value = sum(temps)/len(temps)
    elif _option == "max":
        value = max(temps)
    elif _option == "min":
        value = min(temps)

    return value


# Get all cities in the given _country
def get_all_city(_country):
    cities_temp = []
    for city in cities:
        if city['country'] == _country:
            cities_temp.append(city['city'])
    
    return cities_temp


# All city in Italy
print("All the cities in Italy :")
print(get_all_city("Italy"))
print()

# Let's write code to
# - print the average temperature for all the cities in Italy
print(f"The average temperature of all the cities in Italy :")
print(temperature("Italy", "avg"))
print()

# - print the average temperature for all the cities in Sweden
print(f"The average temperature of all the cities in Sweden :")
print(temperature("Sweden", "avg"))
print()

# - print the min temperature for all the cities in Italy
print(f"The min temperature of all the cities in Italy :")
print(temperature("Italy", "min"))
print()

# - print the max temperature for all the cities in Sweden
print(f"The max temperature of all the cities in Sweden :")
print(temperature("Sweden", "max"))
print()