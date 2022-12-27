x = int(input("enter the value of x:"))

# PLEASE NOTE IN PYTHON THERE ARE NO NEED FOR break STATEMENTS FOR match-case
match x:  #matching the value of x
  case 0: #if x is 0
    print("x is zero")
  case 4: #if x is 4
    print("x is four")
  case default:
    print("dont know")