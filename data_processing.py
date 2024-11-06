import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def read_file(file_name, location=__location__): #wrote a function to read file
    tmp = []
    with open(os.path.join(location, file_name)) as f:
        rows = csv.DictReader(f)
        for r in rows:
            tmp.append(dict(r))
    
    return tmp

###################### CLASS ########################

class Table:

    def __init__(self, table_name, table):
        self.__table_name = table_name
        self.__table = table

    def filter(self, _condition):
        filtered_list = []
        for item in self.__table:
            if _condition(item):
                filtered_list.append(item)
        self.__table = filtered_list

    def aggregate(self, _aggregation_key, _aggregation_function):
        temp = []
        for item in self.__table:
            temp.append(float(item[_aggregation_key]))
        return _aggregation_function(temp)
    
    def __str__(self) -> str:
        final_str = f"\nTABLE: {self.__table_name}\n"

        for key in dict.keys(self.__table[0]):
            final_str += f"{key:22} "
        final_str += "\n\n"
        
        for row in range(len(self.__table)):
            for key in dict.keys(self.__table[0]):
                final_str += f"{self.__table[row][key]:22} "
            final_str += "\n"
        return final_str
        
    @property
    def name(self): #Extra Getter method
        return self.__table_name
    
    @name.setter
    def name(self, name): #Extra Setter method
        self.__table_name = name


class TableDB:

    def __init__(self) -> None:
        self.__table_db = []
    
    def insert(self, table):
        self.__table_db.append(table)
    
    def search(self, table_name):
        for table in self.__table_db:
            if table.name == table_name:
                return table
        return None
    
    def __str__(self) -> str: #
        final_str = "\nCURRENT DATABASE:\n"
        for table in self.__table_db:
            final_str += f"{table.name}\n"
        
        return final_str


####################### MAIN #########################
# Read csv files
cities = read_file('Cities.csv')
countries = read_file('Countries.csv')

# Put the data in TableDB
big_data = TableDB()
big_data.insert(Table("Italy", cities))
big_data.insert(Table("Sweden", cities))
big_data.insert(Table("Country", countries))
print(big_data)

# Filter to get Sweden and Italy datas
italy_data = big_data.search("Italy")
sweden_data = big_data.search("Sweden")

italy_data.filter(lambda x: x['country'] == "Italy")
sweden_data.filter(lambda x: x['country'] == "Sweden")

# Let's see if it works
print(italy_data)
print(sweden_data)

# Lamba functions
f_min = lambda x : min(x)
f_avg = lambda x : sum(x)/len(x)
f_max = lambda x : max(x)
# Let's write code to

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

######################## UNUSED ############################

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