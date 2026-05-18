# Episode 4 — Python Lists Explained
## lists.txt

---

# Creating a Basic List

## Code

```python
temperatures = [22, 25, 27, 30]
print(temperatures)
```

## Output

```python
[22, 25, 27, 30]
```

---

# Accessing Values by Index

## Code

```python
temperatures = [22, 25, 27, 30]
print(temperatures[0])
```

## Output

```python
22
```

---

# Accessing Another Index

## Code

```python
temperatures = [22, 25, 27, 30]
print(temperatures[2])
```

## Output

```python
27
```

---

# Negative Indexing

## Code

```python
temperatures = [22, 25, 27, 30]
print(temperatures[-1])
```

## Output

```python
30
```

---

# Appending a New Value

## Code

```python
temperatures = [22, 25, 27, 30]
temperatures.append(33)
print(temperatures)
```

## Output

```python
[22, 25, 27, 30, 33]
```

---

# Updating a Value

## Code

```python
temperatures = [22, 25, 27, 30, 33]
temperatures[1] = 26
print(temperatures)
```

## Output

```python
[22, 26, 27, 30, 33]
```

---

# Looping Through a List

## Code

```python
temperatures = [22, 26, 27, 30, 33]

for temperature in temperatures:
    print("Temperature:", temperature)
```

## Output

```python
Temperature: 22
Temperature: 26
Temperature: 27
Temperature: 30
Temperature: 33
```

---

# Using Conditions Inside a Loop

## Code

```python
temperatures = [22, 26, 27, 30, 33]

for temperature in temperatures:
    if temperature > 30:
        print("⚠️ High temperature detected:", temperature)
    else:
        print("Normal temperature:", temperature)
```

## Output

```python
Normal temperature: 22
Normal temperature: 26
Normal temperature: 27
Normal temperature: 30
⚠️ High temperature detected: 33
```

---

# Average Temperature

## Code

```python
average_temperature = sum(temperatures) / len(temperatures)
print("Average temperature:", average_temperature)
```

## Output

```python
Average temperature: 27.6
```

---

# Highest and Lowest Values

## Code

```python
print("Highest temperature:", max(temperatures))
print("Lowest temperature:", min(temperatures))
```

## Output

```python
Highest temperature: 33
Lowest temperature: 22
```

---

# String Lists

## Code

```python
systems = ["Cooling", "Navigation", "Battery", "Sensors"]
print(systems)
```

## Output

```python
['Cooling', 'Navigation', 'Battery', 'Sensors']
```

---

# Accessing String Values

## Code

```python
print(systems[0])
```

## Output

```python
Cooling
```

---

# Looping Through Strings

## Code

```python
for system in systems:
    print("System:", system)
```

## Output

```python
System: Cooling
System: Navigation
System: Battery
System: Sensors
```

---

# Mixed Data Types

## Code

```python
mixed_data = [25, "Battery", True]
print(mixed_data)
```

## Output

```python
[25, 'Battery', True]
```

---

# Creating an Empty List

## Code

```python
sensor_readings = []
print(sensor_readings)
```

## Output

```python
[]
```

---

# Dynamically Adding Values

## Code

```python
sensor_readings = []

sensor_readings.append(22)
sensor_readings.append(24)
sensor_readings.append(27)

print(sensor_readings)
```

## Output

```python
[22, 24, 27]
```

---

# Random Sensor Generation

## Code

```python
import random

sensor_readings = []

for i in range(5):
    reading = random.randint(20, 35)
    sensor_readings.append(reading)

print(sensor_readings)
```

## Example Output

```python
[24, 31, 22, 28, 35]
```

---

# Searching Inside a List

## Code

```python
sensor_readings = [24, 31, 22, 28, 35]
print(31 in sensor_readings)
```

## Output

```python
True
```

---

# Searching for Missing Values

## Code

```python
print(100 in sensor_readings)
```

## Output

```python
False
```

---

# Combining Search with Conditions

## Code

```python
if 35 in sensor_readings:
    print("Critical reading detected.")
```

## Output

```python
Critical reading detected.
```

---

# Scanning Through Data

## Code

```python
for reading in sensor_readings:
    if reading > 30:
        print("⚠️ High reading:", reading)
```

## Output

```python
⚠️ High reading: 31
⚠️ High reading: 35
```

---

# Removing Values

## Code

```python
sensor_readings = [24, 31, 22, 28, 35]

sensor_readings.remove(22)
print(sensor_readings)
```

## Output

```python
[24, 31, 28, 35]
```

---

# Removing the Last Value

## Code

```python
sensor_readings.pop()
print(sensor_readings)
```

## Output

```python
[24, 31, 28]
```

---

# Removing by Index

## Code

```python
sensor_readings.pop(1)
print(sensor_readings)
```

## Output

```python
[24, 28]
```

---

# Final Reminder

Lists are one of the foundational structures in programming.

They allow systems to:
- organize memory
- process collections of data
- grow dynamically
- search information
- and evolve over time

Educational demonstration only — not medical or clinical use.

Complexity isn’t our enemy — it’s nature waiting to be understood.

