#TYPECASTING

#this day we learn about typecasting , 

a = "1"
b = "2"

print(a+b) #this prints 12 as both are set as string 

#typecasting is the conversion of a datatype to another datatype

print(int(a)+int(b)) #here a and b are being converted to integer before the addition thus it prints 3

#explicit and implicit type casting

#explicit typecasting is when the programmers manually converts a data to another type
print(int(a)+int(b)) #in this strings are being converted to int , this was done by using a function int() , not done automatically by puthon interpreter

#implicit type is when python interpreter automatically typecasts the value
c = 1.2
d = 4

print(c+d) #here the int value d is converted to float and then added the the result is given in float