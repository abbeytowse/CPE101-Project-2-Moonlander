# Project 2 - Moonlander
#
# Author: Abbey Towse
# Section: CPE 101-11
# Date: 4/16/2021


def showWelcome():
    """
    Input type: none
    Output type: string
    Gives welcome message
    """
    print("Welcome aboard the Lunar Module Flight Simulator\n\n"
          "\tTo begin you must specify the LM's initial altitude\n"
          "\tand fuel level. To simulate the actual LM use\n"
          "\tvalue of 1300 meters and 500 liters, respectively.\n\n"
          "\tGood luck and may the force be with you!\n")


def getFuel():
    """
    Input type: string
    Output type: integer
    Asks for fuel amount
    """
    # Want to code for if user input is a string that can't be type converted
    # to a integer. Don't know how.

    while True:

        fuel = input("Enter the initial amount of fuel on board of the LM "
                     "(in liters): ")
        fuel = int(fuel)

        if fuel >= 0:

            break

        else:

            print("ERROR: Amount of fuel must be positive, please try again")

    return fuel


def getAltitude():
    """
    Input type: string
    Output type: float
    Asks for altitude level
    """
    # Want to code for if user input is a string that can't be type converted
    # to a float. Don't know how.

    while True:

        altitude = input("Enter the initial altitude of the LM (in meters): ")
        altitude = float(altitude)

        if 9999 >= altitude >= 1:

            break

        else:

            print("ERROR: Altitude must be between 1 and 9999, inclusive, "
                  "please try again")

    return altitude


def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
    """
    Input types: integers and floats
    Output type: string
    Displays the state of the LM based on the parameters
    """
    print("Elapsed time: {:>5}".format(elapsedTime), "s")
    print('{:>13}'.format('Fuel:'), '{:>5}'.format(fuelAmount), "l")
    print('{:>13}'.format('Rate:'), '{:>5}'.format(fuelRate), "l/s")
    print('{:>13}'.format('Altitude:'),
          '{:>8}'.format('{:.2f}'.format(altitude)), "m")
    print('{:>13}'.format('Velocity:'),
          '{:>8}'.format('{:.2f}'.format(velocity)), "m/s\n")
    # formatting code style from pyformat.info
    return


def getFuelRate(currentFuel):
    """
    Input type: integer
    Output type: integer
    Gives the remaining fuel level
    """
    # Want to code for if user input is a string that can't be type converted
    # to a integer. Don't know how.

    while True:

        fuelRate = input("Enter fuel rate (0-9, 0=freefall, 5=constant "
                         "velocity, 9=max thrust): ")
        fuelRate = int(fuelRate)

        if 9 >= int(fuelRate) >= 0:

            break

        else:

            print("ERROR: Fuel rate must be between 0 and 9, inclusive, "
                  "please try again")

    return min(fuelRate, currentFuel)


def updateAcceleration(gravity, fuelRate):
    """
    Input types: float and integer, respectively
    Output type: float
    Calculates acceleration given gravity and fuel rate
    """
    acceleration = gravity * ((fuelRate / 5) - 1)
    return acceleration


def updateAltitude(altitude, velocity, acceleration):
    """
    Input types: floats
    Output type: float
    Calculates altitude given altitude, velocity, and acceleration
    """
    altitude = altitude + velocity + (acceleration / 2)
    return max(altitude, 0)


def updateVelocity(velocity, acceleration):
    """
    Input types: floats
    Output type: float
    Calculates velocity given velocity and acceleration
    """
    velocity = velocity + acceleration
    return velocity


def updateFuel(fuel, fuelRate):
    """
    Input types: integers
    Output types: integer
    Calculates fuel given fuel and fuel rate
    """
    fuel = fuel - fuelRate
    return max(fuel, 0)


def displayLMLandingStatus(velocity):
    """
    Input type: float
    Output type: string
    Gives landing status based on velocity
    """
    if 0 >= velocity >= -1:

        print("Status at landing - The eagle has landed!")

    elif -1 > velocity > -10:

        print("Status at landing - Enjoy your oxygen while it lasts!")

    elif velocity <= -10:

        print("Status at landing - Ouch - that hurt!")
