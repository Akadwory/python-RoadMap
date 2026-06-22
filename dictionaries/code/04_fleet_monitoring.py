"""
TruthZoomX Python Roadmap
Topic: Fleet Monitoring With Lists and Dictionaries

Concepts Covered:
- List of dictionaries
- Looping through multiple systems
- Checking each system state
- Printing system-specific alerts

Engineering Idea:
One dictionary can describe one system.
A list of dictionaries can describe a fleet.
"""

fleet = [
    {
        "id": "DRONE_01",
        "battery": 18,
        "temperature": 45
    },
    {
        "id": "DRONE_02",
        "battery": 82,
        "temperature": 30
    },
    {
        "id": "DRONE_03",
        "battery": 12,
        "temperature": 35
    }
]

print("Fleet health alerts:")

for drone in fleet:
    if drone["battery"] < 20:
        print(drone["id"], "needs charging")

    if drone["temperature"] > 40:
        print(drone["id"], "overheating detected")
