# Project 2 - Moonlander
#
# Author: Abbey Towse
# Section: CPE 101-11
# Date: 4/16/2021

from landerFuncs import *


def main():
    # Display welcome message
    showWelcome()

    # Get initial altitude and fuel levels
    altitude = getAltitude()
    fuel = getFuel()

    # Velocity and fuel rate at time 0
    elapsedTime = 0
    velocity = 0
    fuelRate = 0

    # Display LM status at time 0
    print("LM state at retrorocket cutoff")
    displayLMState(elapsedTime, altitude, velocity, fuel, fuelRate)

    # Get initial fuel rate
    fuelRate = getFuelRate(fuel)

    while altitude > 0:
        # Repeat code until LM reaches the ground

        elapsedTime += 1
        fuel = updateFuel(fuel, fuelRate)
        acceleration = updateAcceleration(1.62, fuelRate)
        altitude = updateAltitude(altitude, velocity, acceleration)
        velocity = updateVelocity(velocity, acceleration)

        if (fuel <= 0) and (altitude > 0):
            # Code runs if LM runs out of fuel while in the air

            fuelRate = 0
            print("OUT OF FUEL - Elapsed Time:", '{:>3}'.format(elapsedTime),
                  "Altitude:", '{:>7}'.format('{:.2f}'.format(altitude)),
                  " Velocity:", '{:>7}'.format('{:.2f}'.format(velocity)))
            # formatting code style from pyformat.info

        elif altitude > 0:
            # Code runs if LM is in the air and has fuel remaining

            displayLMState(elapsedTime, altitude, velocity, fuel, fuelRate)
            fuelRate = getFuelRate(fuel)

    # Display LM status at landing
    print("\nLM state at landing/impact")
    displayLMState(elapsedTime, altitude, velocity, fuel, fuelRate)
    displayLMLandingStatus(velocity)


main()
