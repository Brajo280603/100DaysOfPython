#STRINGS
str1 = "this is a string"
str2 = 'strings can also be written with single quotes'

print(str1+"\n"+str2)
str3 = "example"
print(str3[0])
print(str3[1])
print(str3[2])
print(str3[3])
print(str3[4])
print(str3[5])
print(str3[6])
#strings can be printed as a array of characters

str4 = "to pass double quotes(\") use \\ as the escape sequence\n"

str5 = '''use triple single quote 
to pass a multiline string'''

print(str4+"\n"+str5)

str6 = """
triple double quotes can 
also be used to pass multiline string"""

print(str6)


print("\n printing strings as characters using for loop")
for character in str2:
	print(character)
