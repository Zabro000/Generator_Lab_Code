from Phidget22.Phidget import *
from Phidget22.Devices.CurrentInput import *
import time
import csv

#https://www.phidgets.com/?view=api&product_id=VCP1100_0&lang=Python


CurrentSensor = CurrentInput()
TimeReading = 30 #seconds
ReadingInterval = 0.02
CSVfile= "Generator A vs C.csv"


while True:
    try:
        CurrentSensor.openWaitForAttachment(1000)
    except PhidgetException:
        print("Something went wrong with the connecting the phidgets to the computer")
    finally:
        print("Everythng is good")
        break 


print("If ready press any key ALSO CLOSE THE CSV FILE")
input()
print('\n')

Startingtime = time.time()
print("The starting unix time is: ", Startingtime)
time.sleep(1)
print("Second callibration: ", time.time() - Startingtime)
Currentlist = []
Secondlist = []
print(f"The loop is starting and it will run for {TimeReading} seconds.")
print('\n')

# Reassign time just so everything is accurate
Startingtime = time.time()
CurrentTime = time.time()

while CurrentTime - Startingtime < TimeReading:
    Currentlist.append(CurrentSensor.getCurrent())
    Secondlist.append(time.time() - Startingtime)
    CurrentTime = time.time()
    print(Currentlist[-1])
    time.sleep(ReadingInterval)
    


CurrentSensor.close()
print('\n')
print(f"The reading is done,the length of the time(s) list is {len(Secondlist)} and the length of the current(A) list is {len(Currentlist)}")
print("writing the data to a csv file, top row is current and bottom row is time")



with open(CSVfile, 'w') as CSV:
    Writer = csv.writer(CSV)
    #First row is the current in amps
    Writer.writerow(Currentlist)
    #Second row is the time in seconds
    Writer.writerow(Secondlist) 
    






print("Everything is done")


