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

# # Get average, min or max temperature of the give _country
# def temperature(_country, _option):
#     temps = []
#     for city in cities:
#         if city['country'] == _country:
#             temps.append(float(city['temperature']))
    
#     if _option == "avg":
#         value = sum(temps)/len(temps)
#     elif _option == "max":
#         value = max(temps)
#     elif _option == "min":
#         value = min(temps)

#     return value


# # Get all cities in the given _country
# def get_all_city(_country):
#     cities_temp = []
#     for city in cities:
#         if city['country'] == _country:
#             cities_temp.append(city['city'])
    
#     return cities_temp

################################################

class DataProcessing:

    def __init__(self, _dict_list) -> None:
        self.dict_list = _dict_list

    def filter(self, _condition):
        filtered_list = []
        for item in self.dict_list:
            if _condition(item):
                filtered_list.append(item)
        self.dict_list = filtered_list

    def aggregate(self, _aggregation_key, _aggregation_function):
        temp = []
        for item in self.dict_list:
            temp.append(float(item[_aggregation_key]))
        return _aggregation_function(temp)

f_min = lambda x : min(x)
f_avg = lambda x : sum(x)/len(x)
f_max = lambda x : max(x)

italy_data = DataProcessing(cities)
sweden_data = DataProcessing(cities)

italy_data.filter(lambda x: x['country'] == "Italy")
sweden_data.filter(lambda x: x['country'] == "Sweden")

# Let's write code to
print()

# - print the average temperature for all the cities in Italy
print("print the average temperature for all the cities in Italy")
print(italy_data.aggregate("temperature", f_avg))
print()

# - print the average temperature for all the cities in Sweden
print("print the average temperature for all the cities in Sweden")
print(sweden_data.aggregate("temperature", f_avg))
print()

# - print the min temperature for all the cities in Italy
print("print the min temperature for all the cities in Italy")
print(italy_data.aggregate("temperature", f_min))
print()

# - print the max temperature for all the cities in Sweden
print("print the max temperature for all the cities in Sweden")
print(sweden_data.aggregate("temperature", f_max))
print()

