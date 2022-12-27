#IF ELSE CONDITIONS
budget = 500
price = int(input("Enter the price:"))

if (price>budget):
  print("you cannot afford")
elif (price == budget):
  print("you can afford , but not recommended")
  #in python indentation matters , this comment is in elseif(elif) block
else:
  print("you can afford, buy it now")
  #this one is in else block
#this is outside 

#nested if else statements can be written using indentation