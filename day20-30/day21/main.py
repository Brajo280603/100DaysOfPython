# def average(a,b): #here a and b are required arguments as the function uses a and b inside
#   print("the average is ", (a+b)/2)

# average(10,30)

# def average(a=5,b=10): #here a and b have a default value thus the value 5,10 are default arguments of this function 
#   print("the average is ", (a+b)/2)

# average()


# def average(a=5,b=10): #here a and b have a default value thus the value 5,10 are default arguments of this function 
#   print("the average is ", (a+b)/2)


# def average(*nums): #this takes arguments as tuples (arrays)
#   for i in nums:
#     sum = sum+i
#   print("Average is:", sum/len(nums))


# def name(**name):
#   print("Hello,",name["fname"],name["mname"],name["lname"])

# objects = {

# }

# print(objects)
# name(  fname="chinnaswami",
#   mname="muttuswami",
#   lname="venugopala iyer")

def returnsavg(a,b):
  return (a+b)/2

avg = returnsavg(5,6)

print(avg)