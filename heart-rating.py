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

#first we create a input to determine user's age
age = int(input("Please enter your age: "))

#then we stablished the formula to express the 65% and 85% of the range 
range = int(220 - age)
min_range = int(0.65 * range)
max_range = int(0.85 * range)

#at the end show the display of the results of the formula 
print("When you exercise to strengthen your heart, you should keep your heart rate \nbetween", (min_range), "and", (max_range) ,"beats per minute.")