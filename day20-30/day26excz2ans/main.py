#EXCERSIZE 2 ANS


import time 

t = time.strftime('%H:%M:%S')

hour = int(time.strftime("%H"))
print(t)
print(hour)

if(hour>0 and hour<12):
  print("Good Morning Sir!")
elif(hour==12):
  print("Good Noon Sir!")
elif(hour>12 and hour<18):
  print("Good AfterNoon Sir!")
elif(hour>=18):
  print("Good Evening Sir!")