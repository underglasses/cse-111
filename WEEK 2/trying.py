"""
Many vehicle owners record the fuel efficiency of their vehicles as a way to track 
the health of the vehicle. If the fuel efficiency of a vehicle suddenly drops, 
there is probably something wrong with the engine or drive train of the vehicle. 
In the United States, fuel efficiency for gasoline powered vehicles is calculated 
as miles per gallon. In most other countries, 
fuel efficiency is calculated as liters per 100 kilometers.

The formula for computing fuel efficiency in miles per gallon is the following:

mpg = (end - start) / gallons
where start and end are both odometer values in miles and gallons is a fuel amount in U.S. gallons.

The formula for converting miles per gallon to liters per 100 kilometers is the following:

lp100k = 235.215 / mpg
"""
"""
Write a Python program that asks the user for three numbers:

- A starting odometer value in miles
- An ending odometer value in miles
- An amount of fuel in gallons
Your program must calculate and print fuel efficiency in both miles per gallon 
and liters per 100 kilometers. Your program must have three functions named as follows:

- main
- miles_per_gallon
- lp100k_from_mpg
All user input and printing must be in the main function. In other words, 
the miles_per_gallon and lp100k_from_mpg functions must not call 
the input or print functions.

"""

import math
import time


def main():
    welcome()

    start_miles = float(input("Enter the starting odometer value in miles: "))
    end_miles = float(input("Enter the ending odometer value in miles: "))
    amount_gallons = float(input("Enter the amount of fuel in gallons: "))

    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)
    lp100k = lp100k_from_mpg(mpg)

    load_animation()

    print(f"\nFuel efficiency in miles per gallon: {mpg:.1f} mpg")
    time.sleep(1)
    print(f"Fuel efficiency in liters per 100 kilometers: {lp100k:.2f} L/100km")
    time.sleep(1)

    finish()

def welcome():
    print("================================================")
    time.sleep(1)
    print("Welcome to the Fuel Efficiency Calculator!")
    time.sleep(1)
    print("This program will help you calculate your vehicle's fuel efficiency.")
    time.sleep(1)
    print("Let's get started!\n")
    time.sleep(1)

def finish():
    print("\nThank you for using the Fuel Efficiency Calculator!")
    time.sleep(1)
    print("Goodbye!")
    time.sleep(1)
    print("================================================")

def load_animation():
    print("\n")
    #animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    animation = ["Calculating.","Calculating..","Calculating..."]
    for i in range(len(animation)):
        time.sleep(0.5)
        print("\r" + animation[i % len(animation)], end="")
    print("\n")

def miles_per_gallon(start_miles, end_miles, amount_gallons):
    mpg = abs(end_miles - start_miles) / amount_gallons
    return (mpg)

def lp100k_from_mpg(mpg):

    lp100k = 235.215 / mpg
    return lp100k

main()
