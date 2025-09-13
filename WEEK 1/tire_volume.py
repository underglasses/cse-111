""" Marcos Chinga | Programming with functions CSE 111 | Tire Volume Calculator """

"""
The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters. The second number is the aspect ratio. 
The third number is the diameter in inches of the wheel that the tire fits. 
The volume of space inside a tire can be approximated with this formula:
"""
"""
v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
"""
#the time library is imported to make the program feel more dynamic
import math
import time
from datetime import datetime

# welcome message
print("Welcome to the Tire Volume Calculator \n")

# user inputs for width, aspect ratio and diameter
w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

#this is a calculation print statement just to feeling more dynamic
print("\nCalculating the tire volume")
time.sleep(1)
print("\n.","\n.","\n.")
time.sleep(1)
print("\nDone!") 
time.sleep(1) 

# calculation for volume
volume = (((math.pi * (w**2) * a)) * ((w * a) + (2540 * d)) / 10000000000)

# showing the result to the user
print(f"\nThe approximante volume is: {volume: .2f} liters")

# rounding the volume to 2 decimal points
total = round(volume, 2)
today = datetime.now()
today = f"{today: %Y-%m-%d}"

# writing to a file, I add a separator to make it more readable
with open('volumes.txt', "a") as volumes_file:
    volumes_file.write(f"\nCurrent date: {str(today)}"
                      f"\nWidth = {str(w)}"
                      f"\nAspect ratio of the tire is = {str(a)}"
                      f"\nDiameter of the wheel is = {str(d)}"
                      f"\nVolume of the tire is = {str(total)}"
                      f"\n------------------------------")