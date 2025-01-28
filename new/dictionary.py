person={"name":"Shinsuke Ito","age":"30","city":"prague"}
print(person["name"])
person["professional"]="Data Scientist"
del person["age"]
for key, value in person.items():
    print(f"{key}:{value}")