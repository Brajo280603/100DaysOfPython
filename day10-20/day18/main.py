# for i in range(3):
#   print(i)

# # same thing with while loop
# i=0
# while(i<3):
#   print(i)
#   i=i+1


# i = int(input("enter the value of i:"))

# while(i<38):
#   i = int(input("enter the value of i which is more than 38:"))
#   print(i,"is smaller than 38")

# print(i,"is bigger than 38")

#there are no do while loop in python ,to emulate do while just run the contents of while loop before the loop starts

i = int(input("enter the value of i which is more than 38:"))
print(i,"is smaller than 38")
while(i<38):
  i = int(input("enter the value of i which is more than 38:"))
  print(i,"is smaller than 38")