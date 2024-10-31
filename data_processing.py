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

################################################

def filter(condition, dict_list):
    filtered_list = []
    for item in dict_list:
        if condition(item):
            filtered_list.append(item)
    return filtered_list

def aggregate(_aggregation_key, _aggregation_function, _dict_list):
    temp = []
    for item in _dict_list:
        temp.append(float(item[_aggregation_key]))
    return _aggregation_function(temp)

f_min = lambda x : min(x)
f_avg = lambda x : sum(x)/len(x)
f_max = lambda x : max(x)

# Let's write code to
# - print the average temperature for all the cities in Italy
print("print the average temperature for all the cities in Italy")
x = filter(lambda x: x['country'] == "Italy", cities)
print(aggregate("temperature", f_avg, x))
print()

# - print the average temperature for all the cities in Sweden
print("print the average temperature for all the cities in Sweden")
x = filter(lambda x: x['country'] == "Sweden", cities)
print(aggregate("temperature", f_avg, x))
print()

# - print the min temperature for all the cities in Italy
print("print the min temperature for all the cities in Italy")
x = filter(lambda x: x['country'] == "Italy", cities)
print(aggregate("temperature", f_min, x))
print()

# - print the max temperature for all the cities in Sweden
print("print the max temperature for all the cities in Sweden")
x = filter(lambda x: x['country'] == "Sweden", cities)
print(aggregate("temperature", f_max, x))
print()

