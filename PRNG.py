M = eval(input("please enter how many codes you want generated: "))
count = 0
while count < M: 
#importing date and time
 import time 
 time.sleep(1) 
 from datetime import datetime
 now = datetime.now()
#defining each number of the date and time as a variable
 x = (now.strftime("%Y"))
 y = (now.strftime("%m"))
 z = (now.strftime("%d"))
 f = (now.strftime("%H")) 
 g = (now.strftime("%M"))
 h = (now.strftime("%S"))
#adding up all the variables in order to generate a new seed every second
 dateseed = int(x) + int(y) + int(z) + int(f) + int(g) + int(h)
#making sure that the number will never exceed 4 digits
 if dateseed > 9999: dateseed//= 10


 def rng(m=7, a=5, c=9):
    global dateseed
    dateseed = ((a*dateseed + c)*dateseed) 
    return dateseed
 if dateseed > 99999999: dateseed//= 10 
 print(rng())
 count = count + 1
 