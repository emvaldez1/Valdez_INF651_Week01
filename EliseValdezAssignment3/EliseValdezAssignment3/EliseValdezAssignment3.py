# INF360 - Programming in Python
# Elise Valdez
# Assignment 3

# Create dictionaries for each vehicle that contains the fields/keys and values listed above.
vehicles = [
    {"name": "Ka", "year_introduced": 1996, "production_current_model": 2014, "generation": "3rd", "vehicle_information": "Developed by Ford Brazil as a super mini car"},
    {"name": "Fiesta", "year_introduced": 1976, "production_current_model": 2017, "generation": "7th", "vehicle_information": "Ford's long running subcompact line based on global B-car Platform"},
    {"name": "Focus", "year_introduced": 1998, "production_current_model": 2018, "generation": "3rd", "vehicle_information": "Ford's Compact car based on global C-car platform"},
    {"name": "Mondeo", "year_introduced": 1992, "production_current_model": 2012, "generation": "2nd", "vehicle_information": "Mid sized passenger sedan with 'One-Ford' design based on CD4 platform"},
    {"name": "Fusion", "year_introduced": 2005, "production_current_model": 2014, "generation": "5th", "vehicle_information": "Similar to Mondeo"},
    {"name": "Taurus", "year_introduced": 1986, "production_current_model": 2009, "generation": "6th", "vehicle_information": "Full sized car based on D3 platform"},
    {"name": "Fiesta ST", "year_introduced": 2013, "production_current_model": 2013, "generation": "1st", "vehicle_information": "Fiesta's high performance factory tune"},
    {"name": "Focus RS", "year_introduced": 2015, "production_current_model": 2015, "generation": "1st", "vehicle_information": "Special high performance Focus developed by SVT"},
    {"name": "Mustang", "year_introduced": 1964, "production_current_model": 2014, "generation": "6th", "vehicle_information": "Ford's long running pony/muscle car"},
    {"name": "GT", "year_introduced": 2004, "production_current_model": 2016, "generation": "2nd", "vehicle_information": "Ford's limited production super car inspired by the legendary race car GT40"}
]

# Function to convert a list of vehicle dictionaries to a dictionary with the 'name' as the key
def listToDict(vehicle_list):
    return {vehicle["name"]: vehicle for vehicle in vehicle_list}

# Convert the list of vehicles to a dictionary
vehicles_dict = listToDict(vehicles)

# Function to return a list of car names sorted alphabetically
def getSortedCarNames(vehicle_dict):
    return sorted(vehicle_dict.keys())

# Get sorted car names
sorted_car_names = getSortedCarNames(vehicles_dict)

# Function to return a dictionary of car names and their year of introduction
def getCarNamesAndYears(vehicle_dict):
    return {name: details["year_introduced"] for name, details in vehicle_dict.items()}

# Get car names and their years of introduction
car_names_and_years = getCarNamesAndYears(vehicles_dict)

# Print sorted car names, each on their own line
print("Sorted car names:")
for name in sorted_car_names:
    print(name)

# Print car names and years introduced, sorted by year introduced
print("\nCars sorted by year introduced:")
for name, year in sorted(car_names_and_years.items(), key=lambda item: item[1]):
    print(f"{year} : {name}")
