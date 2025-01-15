import pandas
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
a=[1,7,2]
myvar = pandas.DataFrame(mydataset)
k=pandas.Series(a,index=["x","y","z"])
print(myvar.loc[0])
print(k)