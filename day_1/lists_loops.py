cities = ["London", "Paris", "Berlin", "New York"]
print("Cities in dataset:\n")
for city in cities:
    print(city) 

print("Cities in dataset once again:\n")
for i, city in enumerate(cities, start=1):
    print(i, " - ", city)
     