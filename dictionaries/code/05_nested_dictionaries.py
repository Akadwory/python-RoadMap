"""
TruthZoomX Python Roadmap
Topic: Nested Dictionaries

Concepts Covered:
- Dictionaries inside dictionaries
- Organizing systems into subsystems
- Accessing nested values
- Updating nested values

Engineering Idea:
Real machines are systems made of subsystems.
Nested dictionaries help software represent that structure.
"""

# A drone organized into subsystems.
drone = {
    "id": "DRONE_01",
    "power": {
        "battery": 50,
        "voltage": 12.1
    },
    "navigation": {
        "gps": "ONLINE",
        "altitude": 250
    }
}

print("Full drone structure:")
print(drone)

print("\nAccessing nested values:")
print("Battery:", drone["power"]["battery"])
print("Voltage:", drone["power"]["voltage"])
print("GPS:", drone["navigation"]["gps"])
print("Altitude:", drone["navigation"]["altitude"])

# Update nested battery value.
drone["power"]["battery"] = 18

print("\nUpdated battery after drone use:")
print("Battery:", drone["power"]["battery"])
