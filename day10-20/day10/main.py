string = input("enter a string:")
integer = int(input("enter an integer:"))
floating = float(input("enter a floating point number:"))
print("this is a string:"+string)
print("this is an integer:",integer)
print("this is a floating point number:",floating)


#this was done as the doing all the operations with inputs as integer and strings
a = input("enter number a: ")
b = input("enter number b: ")

print("all operations as string")
print("addition:",a+b)          #all operations other than addition(concat) are invalid for string data type 
#print("substraction",a-b)
#print("multiplication",a*b)
#print("division",a/b)
#print("modulus",a%b)

print("\nall operations as integer")
print("addition:",int(a)+int(b))
print("substraction",int(a)-int(b))
print("multiplication",int(a)*int(b))
print("division",int(a)/int(b))
print("modulus",int(a)%int(b))
