#EXCERSIZE 2 : GOOD MORNING SIR!
#excersize goodmorning sir
import time

timestamp = int(time.strftime("%H"))

name = input("Enter your name:")

if(timestamp<12):
  print("good morning,"+name)
elif(timestamp>12 and timestamp<18):
  print("good afternoon,"+name)
else:
  print("good evening,"+name)
