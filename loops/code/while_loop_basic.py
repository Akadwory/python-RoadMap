"""
===========================================
Basic While Loop Example
===========================================

Description:
This program demonstrates how a basic
while loop works in Python.

A while loop continues running
as long as a condition remains true.

Concepts Covered:
- while Loops
- Conditions
- Repetition
- Variables
- Loop Control

Author:
TruthZoomX

Purpose:
Teach how systems continuously repeat
behavior based on conditions.
===========================================
"""


# ----------------------------------------
# Initial System State
# ----------------------------------------

# Starting battery value
battery_level = 5


# ----------------------------------------
# Main While Loop
# ----------------------------------------

# Continue looping while battery is above 0
while battery_level > 0:

    # Display current battery value
    print("Battery:", battery_level)

    # Reduce battery level
    battery_level -= 1


# ----------------------------------------
# System Shutdown Message
# ----------------------------------------

print("Battery depleted.")
print("System shutting down.")