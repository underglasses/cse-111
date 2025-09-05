"""
MARCOS CHINGA CSE 111| PROGRAMMING WITH FUNCTIONS | HEART RATING
"""

"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
#This libary is for personal details
import time

print("Welcome to the Heart Rate Calculator \n")
time.sleep(1)

#first we create a input to determine user's age
age = int(input("Please enter your age: "))
time.sleep(1)

#then we stablished the formula to express the 65% and 85% of the range 
range = int(220 - age)
min_range = int(0.65 * range)
max_range = int(0.85 * range)

#this is a calculation print statement just to feeling
print("\nCalculating your heart rate range")
time.sleep(1)
print("\n.","\n.","\n.")
time.sleep(1)
print("\nDone!") 
time.sleep(1) 

#at the end show the display of the results of the formula 
print("\nWhen you exercise to strengthen your heart, you should keep your heart rate \nbetween", (min_range), "and", (max_range) ,"beats per minute.")
time.sleep(1)

#finally we create a print statement
print("\nThank you for using the Heart Rate Calculator!")
time.sleep(1)