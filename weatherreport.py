Weaterinfo = {
    "Delhi"    : {"temp" : 31 , "Condition" : "Sunny"},
    "Mumbai"    : {"temp" : 21 , "Condition" : "cloudy"},
    "Pune"    : {"temp" : 41 , "Condition" : "rainy"},
    "Mizoram"    : {"temp" : 51 , "Condition" : "humid"},
    }
cities = input("Enter the city to get its weather report : ").split(",")
for city in cities:
    city.strip().title()
    
    if city in Weaterinfo:
        print(f"{city} => Temp : {Weaterinfo[city]['temp'] }°C , Condition : {Weaterinfo[city]['Condition']}")
    else:
        print(f"Invalid {city} not found>>>>>>>>")