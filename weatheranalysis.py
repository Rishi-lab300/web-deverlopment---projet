import numpy as np
weather = np.random.randint(1,50)
print(f"Weather : {weather}°C ")
full_year = np.random.randint(1,50,size =30)
print("Temperatures for a year : " , full_year)
print("Maximum temperture in a year : " , full_year.max())
print("Minimum temperture in a year : " , full_year.min())

avg_forayear = full_year.mean()
print("average temperature of the year : " , avg_forayear)
if weather<=20:
    print(f"{weather}°C is the temperature for winter...")
else:
    print(f"{weather}°C is the temperature for summer")