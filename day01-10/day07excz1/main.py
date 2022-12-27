#EXCERSIZE 1: CALCULATOR USING PYTHON

print(1+3) #addition operator
print(3-3) #substraction operator
print(3*6) #multiplication operator
print(81/4) #division operator 
print(344%3) #modulo operator , returns the remainder
print(5**3) #exponent operator, returns the exponent


#the calendar excersize

print("####################      CALCULATOR      ##################### ")
num1 = input("enter first number : ")
num1 = int(num1)
num2 = input("enter second number : ")
num2 = int(num2)
print("1: addition\n2: substraction\n3: multiplication\n4: division\n5: remainder\n6: exponent ")
operation = input("operation : ")

match operation:#python3 has match to use as the switch statement from other programming language
    case "1":
        print(num1+num2)
    case "2":
        print(num1-num2)
    case "3":
        print(num1*num2)
    case "4":
        print(num1/num2)
    case "5":
        print(num1%num2)
    case "6":
        print(num1**num2)
    case _:
        print("wrong option")
    
