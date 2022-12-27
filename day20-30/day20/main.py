
#this is how you define a function in python
def calGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def passed(a):
  pass #use pass to define a functions definition later

#NOTE first define then use functions in python
a = 9
b = 8

calGmean(a,b)

c = 4
d = 4
calGmean(c,d)

passed(a)