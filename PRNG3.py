#asking user how much random numbers he needs
CNT = eval(input("please enter how many codes you want generated: "))
#configuring while loop in order to operate according to user input
count = 0
#taking seed from txt file
f = open('SEED.txt','r')
total_count = sum(int(x) for x in f if x.strip().isdigit())
seed = total_count
while count < CNT: 
#importing time to let the code run every time interval 
 import time 
 time.sleep(1) 
#importing date and time
 from datetime import datetime
 now = datetime.now()
 print(now.strftime("%d-%m-%Y %H:%M:%S"))
#defining each number of the date and time as a variable
 x = (now.strftime("%Y"))
 y = (now.strftime("%m"))
 z = (now.strftime("%d"))
 f = (now.strftime("%H")) 
 g = (now.strftime("%M"))
 h = (now.strftime("%S"))
 
#adding up all the variables in order to generate a new seed every second

#making sure that the number will never exceed 4 digits
 while seed > 9999: seed//= 10
 print(("seed: "),seed)

#defining the algorithim that the code will run on 
 import random
 value = int(random.uniform(1, 9999)) 
 def rng(m=value, a=value, c=value):
    global seed
    seed = ((a*seed + c)**2) 
    while seed > 99999999: seed//= 10
    return seed
#running the algorithim
 print(("random_number: "),rng())
 count = count + 1
 print(count)