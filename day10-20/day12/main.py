#STRING METHODS
name = "Harry,Subham" 
print(name[0:5]) #this will print the first 5 characters name[initial:end-1]] , 

print(name[:5]) #initial is by default 0

print(name[0:-3]) #negetive value in end , python interpreter adds len(name)-negetiveValue

print(name[-5:10]) #negetive value in initial does the same as end

print(len(name))



#Quick Quiz
nm = "Harry"
print(nm[-4:-2]) #this will result in printing(nm[len(nm)-4:len(nm)-2]) ===> print(nm[5-4:5-2]) =====> print(nm[1:3]) ====>"ar"