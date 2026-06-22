"""
TruthZoomX Python Roadmap
Topic: Dictionary-Based Decisions

Concepts Covered:
- Using dictionary values inside conditions
- Detecting low battery
- Detecting overheating
- Creating reusable health-check logic with a function

Engineering Idea:
The dictionary stores system state.
The condition evaluates system state.
The function packages the behavior for reuse.
"""


def health_check(state):
    """Evaluate a drone state dictionary and print safety alerts."""

    if state["battery"] < 20:
        print("Return to base")

    if state["temperature"] > 40:
        print("Overheating detected")


# Example drone state.
drone_state = {
    "battery": 15,
    "temperature": 45,
    "gps": "ONLINE",
    "altitude": 120,
    "flight_mode": "AUTO"
}

print("Drone health check:")
health_check(drone_state)
