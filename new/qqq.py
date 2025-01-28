# def square_and_cube(x):
#     return x**2, x**3
# square, cube=square_and_cube(3)
# print(f"Square:{square},Cube:{cube}")

# def even(y):
#     if y%2==0:
#         print("even")
#     else:
#         print("odd")
# y=int(input())
# even(y)
age=int(input("your age:"))
if age>20:
    print("adult")
elif age<13:
    print("child")
else:
    print("teenager")
print((age>10)&(age<50))