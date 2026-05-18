"""
TruthZoomX — Python Roadmap
Episode 4: Python Lists Explained — Organizing Memory at Scale

Educational demonstration only — not medical or clinical use.
"""


# 1. Creating a basic list
temperatures = [22, 25, 27, 30]
print("Basic list:", temperatures)


# 2. Accessing values by index
print("First temperature:", temperatures[0])
print("Third temperature:", temperatures[2])
print("Last temperature:", temperatures[-1])


# 3. Adding a new value
temperatures.append(33)
print("After append:", temperatures)


# 4. Updating a value
temperatures[1] = 26
print("After update:", temperatures)


# 5. Looping through a list
print("\nAll temperature readings:")
for temperature in temperatures:
    print("Temperature:", temperature)


# 6. Using conditions inside a loop
print("\nTemperature status:")
for temperature in temperatures:
    if temperature > 30:
        print("High temperature detected:", temperature)
    else:
        print("Normal temperature:", temperature)


# 7. Analyzing the list
average_temperature = sum(temperatures) / len(temperatures)

print("\nTemperature analysis:")
print("Average temperature:", average_temperature)
print("Highest temperature:", max(temperatures))
print("Lowest temperature:", min(temperatures))


# 8. Lists with strings
systems = ["Cooling", "Navigation", "Battery", "Sensors"]

print("\nSystem names:")
for system in systems:
    print("System:", system)


# 9. Mixed data list
mixed_data = [25, "Battery", True]
print("\nMixed data:", mixed_data)


# 10. Building a list dynamically
import random

sensor_readings = []

for i in range(5):
    reading = random.randint(20, 35)
    sensor_readings.append(reading)

print("\nDynamic sensor readings:", sensor_readings)


# 11. Searching inside a list
print("\nSearch results:")
print("Is 31 inside sensor_readings?", 31 in sensor_readings)
print("Is 100 inside sensor_readings?", 100 in sensor_readings)


# 12. Searching with conditions
if 35 in sensor_readings:
    print("Critical reading detected.")


# 13. Scanning through data
print("\nHigh readings:")
for reading in sensor_readings:
    if reading > 30:
        print("High reading:", reading)


# 14. Removing values
sensor_readings = [24, 31, 22, 28, 35]

print("\nOriginal readings:", sensor_readings)

sensor_readings.remove(22)
print("After removing value 22:", sensor_readings)

sensor_readings.pop()
print("After removing last value:", sensor_readings)

sensor_readings.pop(1)
print("After removing index 1:", sensor_readings)


print("\nLists organize memory at scale.")