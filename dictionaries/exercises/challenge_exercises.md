# Challenge Exercises — Engineering Systems With Dictionaries

These exercises are designed to push the concept beyond syntax and into system thinking.

---

## Challenge 1 — Fleet of Vehicles

Create a list called `vehicle_fleet`.

Inside the list, create three dictionaries. Each dictionary should represent one vehicle with:

- `id`
- `speed`
- `fuel`
- `engine_temperature`

Loop through the fleet and print alerts:

- If fuel is below `25`, print that the vehicle needs fuel.
- If engine temperature is above `100`, print that overheating is detected.

---

## Challenge 2 — Nested Vehicle System

Create a nested dictionary called `vehicle` with:

- `power`
  - `fuel`
  - `battery_voltage`
- `navigation`
  - `gps`
  - `speed`
- `diagnostics`
  - `engine_temperature`
  - `fault_code`

Access and print:

- fuel
- speed
- engine temperature

---

## Challenge 3 — Reusable System Health Function

Create a function called `system_health_check(system)`.

The function should check nested values:

- If `system["power"]["fuel"] < 25`, print `Low fuel`
- If `system["diagnostics"]["engine_temperature"] > 100`, print `Engine overheating`
- If `system["navigation"]["gps"] != "ONLINE"`, print `GPS offline`

---

## Challenge 4 — Add Mission State

Add a new nested section called `mission`.

It should include:

- `status`
- `destination`
- `estimated_arrival_minutes`

Then print a sentence like:

```text
Vehicle is heading to Warehouse A and will arrive in 14 minutes.
```

---

## Challenge 5 — Think Like an Engineer

Write a short paragraph answering:

Why is a nested dictionary better than random separate variables when modeling a real machine?

Try to use the words:

- state
- subsystem
- structure
- meaning
- decision
