age=int(input("your age:"))
gender=input()
if(age>18):
    if gender=="male":
        print("Adult male")
    else:
        print("Adult female")
elif(age<18):
    print("you are minor")