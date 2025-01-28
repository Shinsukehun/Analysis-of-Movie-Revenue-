age=int(input("your age:"))
gender=input("your gender")
if(age>18):
    if gender=="male":
        print("Adult male")
    else:
        print("Adult female")
else:
    print("you are minor")