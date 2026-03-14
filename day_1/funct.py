# Demonstrates defining and calling function

def greet(name):
    print(f"Hello: {name}")
    name = "Neeti"

name = input("Enter your name: ")
greet(name)

# I used the same variable name in the function and main code
# Output shows that Change in function doesnt affect main code
if name == "Joy":
    print("Variable defined in global scope is different from function scope")
elif name == "Neeti":
    print("Variable defined in global scope is same as function scope")
else:
    print("Dont know what happened")
