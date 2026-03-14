# Shows how to create a dictionary and loop through it
# Demonstrates the f string of Python
person = {
    "name" : "Joy",
    "age" : 30,
    "city" : "Delhi"    
}

for key, value in person.items():
    print(f"{key}: {value}")
