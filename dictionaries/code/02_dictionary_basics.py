"""
TruthZoomX Python Roadmap
Topic: Dictionary Basics

Concepts Covered:
- Creating a dictionary
- Keys and values
- Accessing values by key
- Updating existing values
- Adding new values

Engineering Idea:
A dictionary allows software to model the state of a real system.
"""

# Create a dictionary that represents a drone state.
drone_state = {
    "battery": 18,
    "temperature": 42,
    "gps": "ONLINE"
}

print("Initial drone state:")
print(drone_state)

# Access values by key.
print("\nAccessing individual values:")
print("Battery:", drone_state["battery"])
print("Temperature:", drone_state["temperature"])
print("GPS:", drone_state["gps"])

# Update values as the drone state changes.
drone_state["battery"] = 15
drone_state["temperature"] = 35

print("\nUpdated drone state:")
print(drone_state)

# Add new information as the system grows.
drone_state["altitude"] = 120
drone_state["flight_mode"] = "AUTO"

print("\nExpanded drone state:")
print(drone_state)
