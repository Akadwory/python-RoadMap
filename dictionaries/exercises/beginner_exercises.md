# Beginner Exercises — Python Dictionaries

These exercises are designed to help you practice the exact concepts from the video.

---

## Exercise 1 — Create a Vehicle State Dictionary

Create a dictionary called `vehicle_state` with the following keys:

- `speed`
- `fuel`
- `engine`

Example values:

```python
speed = 65
fuel = 40
engine = "ON"
```

Print the full dictionary.

---

## Exercise 2 — Access One Value

Using your `vehicle_state` dictionary, print only the fuel value.

Expected idea:

```python
print(vehicle_state["fuel"])
```

---

## Exercise 3 — Update a Value

Change the fuel value from `40` to `25`.

Print the dictionary again and confirm that only the fuel changed.

---

## Exercise 4 — Add New Information

Add a new key called `gps` with the value `"ONLINE"`.

Print the updated dictionary.

---

## Exercise 5 — Make a Decision

Write a condition:

If fuel is below `30`, print:

```text
Refuel soon
```

---

## Exercise 6 — Build a Simple Function

Create a function called `vehicle_check(state)`.

Inside the function:

- If fuel is below `30`, print `Refuel soon`
- If speed is above `80`, print `Reduce speed`

Call the function using your `vehicle_state` dictionary.
