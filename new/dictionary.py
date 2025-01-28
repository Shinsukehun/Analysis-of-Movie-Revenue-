person={"name":"Shinsuke Ito","age":"30","city":"prague"}
print(person["name"])
person["professional"]="Data Scientist"
del person["age"]
for key, value in person.items():
    print(f"{key}:{value}")

def greet(name="Shinsuke"):
    print(f"name:{name}")

greet("Jhonson")
greet()
def min_max(numbers):
    return min(numbers), max(numbers)
nums=[1,5,3,9,7]
x,y=min_max(nums)
print(f"{x},{y}")
square=[x**2 for x in nums]
print(square)