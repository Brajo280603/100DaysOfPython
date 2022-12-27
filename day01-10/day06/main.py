#DATA TYPES

#a variable is a container for storing different types of datas in the ram for temporary use in the program
a = 2323
print(a)
a = "lol" #python auto manages the variable datatypes , so we dont need to declare a variable as a special datatype
print(a) #as you can see the same variable can be reassigned from int to string

#python data types

integer = 123 #the python programming language has a datatype called integer , which stores natural numbers
print("type of integer : ", type(integer))
float = 2.2 #float stores floating point numbers
print("type of float: " , type(float))
cmplx = complex(7,1) #complex datatype stores complex numbers , first part is real , second part is imaginary
print("type of cmplx : ", type(cmplx))
bool = True #boolean datatype , stores true or false value
print("type of bool", type(bool))
string = "string" #string data type , stores string values
print("type of string",type(string))
no = None #NoneType datatype , stores null values/empty
print("type of no: ",type(no))


lists = [0,34,5,5.2,[3,2],["apple", "orange"]] #lists stores a bunch of different datatypes
print("type of lists", type(lists))


tuples = (3,4,2,("lol", "Wth"),(2,3)) #tuple same as lists , except its immutable , meaning cannot be changed
print("type of tuples", type(tuples))

dictionary = { "name":"lolbro" , "actualName" : "nah fam", "ok":"yeah"} #dictionary datatype stores keyvalue pairs , just like js objects or json
print("type of dictionary : ", type(dictionary))

#note everything in python is an object , will be explained later


