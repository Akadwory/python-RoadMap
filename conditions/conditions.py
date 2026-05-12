import random 
import time

fan_on = False 

MAX_TEMP = 70 
MIN_TEMP = 60 

for i in range(10):
    temperature = random.randint(50,80)
    print(f"\nCycle {i+1}: Temperature = {temperature} C ")
    if temperature > MAX_TEMP and not fan_on:
        fan_on =  True
        print("Fan turned ON")
    elif temperature < MIN_TEMP and fan_on:
        fan_on = False
        print("Fan turned OFF")
    else:
        print("No Change. System Stable")
    time.sleep(0.5)

average_last_10_readings = 65
if temperature > average_last_10_readings:
    print("Predicted rising trend >> avtivatung cooling early")