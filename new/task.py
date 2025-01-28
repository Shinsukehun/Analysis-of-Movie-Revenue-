# book={"title":"Python","author":"Shinsuke","year of publication":"1990"}
# print(book["title"])
# for key,content in book.items():
#     print(f"{key},{content}")
import numpy
def sum_and_average(numbers):
    return sum(numbers),numpy.mean(numbers)
nums=[1,2,5,8,3,2,6,8,9]
x,y=sum_and_average(nums)
print(f"sum:{x},average:{y}")
numi=[1,2,3,4,5,6,7,8,9,10]
numj=[x**2 for x in numi]
print(numj)