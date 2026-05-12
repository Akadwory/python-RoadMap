"""
===========================================
Battery Monitoring System Simulation
===========================================

Description:
This program simulates a simple battery
monitoring and charging system using a
while loop.

Concepts Covered:
- Variables
- Boolean Logic
- while Loops
- if Statements
- System State
- Conditional Behavior
- break Statement

Author:
TruthZoomX

Purpose:
Teach how real systems continuously monitor
and react to changing conditions.
===========================================
"""

# ----------------------------------------
# Initial System State
# ----------------------------------------

# Starting battery percentage
battery_level = 100

# Charging state
charging = False


# ----------------------------------------
# Main System Loop
# ----------------------------------------

# Continue running while battery has power
while battery_level > 0:

    # Display current battery percentage
    print("Battery:", battery_level, "%")

    # ------------------------------------
    # Low Battery Detection
    # ------------------------------------

    # If battery is low, enable charging
    if battery_level <= 20:
        charging = True
        print("Low battery detected.")
        print("Charging mode activated.")

    # ------------------------------------
    # Battery Behavior
    # ------------------------------------

    # If charging is active,
    # increase battery percentage
    if charging:
        battery_level += 5

    # Otherwise decrease battery
    else:
        battery_level -= 10

    # ------------------------------------
    # Full Battery Detection
    # ------------------------------------

    # Stop charging when battery is full
    if battery_level >= 100:
        charging = False

    # ------------------------------------
    # Shutdown Protection
    # ------------------------------------

    # Shut down system if battery reaches 0
    if battery_level <= 0:
        print("System shutting down.")
        break