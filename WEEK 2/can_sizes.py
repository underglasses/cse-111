"""
MARCOS CHINGA |CSE 111 | WEEK 2 | CAN SIZES
"""

#by following the sample instructions from the assignment page i just reorganize the code to make it more dinamic and reusable.

"""
Requirements
Your program must compute the volume of all 12 can sizes.
Your program must compute the surface area of all 12 can sizes.
Your program must compute and print the storage efficiency of all 12 can sizes.
Enhancements
Here is a list of enhancements that you could make to the program. 
Your instructor will walk you through at least one of them. 
Feel free to complete others.

1. Add another function named compute_storage_efficiency to your program. 
    This function should call the compute_volume and compute_surface_area functions 
    and then compute and return the storage efficiency of a steel can size. 
    Replace code in the main function with a call to the compute_storage_efficiency function
    as appropriate. Did adding and calling the compute_storage_efficiency function reduce 
    the number of lines of code in your program?

2. The table of can sizes that appears in the Assignment section above includes a column 
    that contains the cost per can of each steel can size. Add another function to your 
    program named compute_cost_efficiency that computes and returns the volume of a 
    steel can divided by its cost. Write code to call the compute_cost_efficiency function
    and print the cost efficiency for each can size. Then visually examine the output and 
    answer this question, “Which can size has the highest cost efficiency?”

3.  If you remember how to use lists and a for loop from CSE 110, rewrite your main 
    function so that it uses a list or lists that contain the can size names and dimensions.
    Then write a loop that processes the values in the list.

4.  Add if statements inside the loop to automatically determine which can size has the
    best storage efficiency and which can size has the best cost efficiency.
"""


import math
import time

def main():
    # A compound list (a list that contains lists).
    can_sizes = [
        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.4, 8.89, 0.22],
        ["#8Z short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.1, 11.11, 0.42]
    ]

    best_store = None
    best_cost = None
    max_store_eff = -1
    max_cost_eff = -1

    # For each can in the can_sizes list, unpack the values
    # into the variables name, radius, height, and cost.

    # Welcome message
    welcome()   

    # Loading animation
    load_animation()

    for i in range(len(can_sizes)):
        name = can_sizes[i][0]
        radius = can_sizes[i][1]
        height = can_sizes[i][2]
        cost = can_sizes[i][3]

        # Call the compute_storage_efficiency and
        # compute_cost_efficiency functions.
        store_eff = compute_storage_efficiency(radius, height)
        cost_eff  = compute_cost_efficiency(radius, height, cost)

        
        # Print the can size name, storage
        # efficiency, and cost efficiency.
        print(f"\n{name} \n -EFFICIENCY: {store_eff:.2f} % \n -COST:       {cost_eff:.0f} $")
        time.sleep(.8)

        # If the storage efficiency of the current can size is
        # greater than the maximum storage efficiency, save then
        # the current can size name and its storage efficiency.
        if store_eff > max_store_eff:
            best_store = name
            max_store_eff = store_eff

        # If the cost efficiency of the current can size is
        # greater than the maximum cost efficiency, then save
        # the current can size name and its cost efficiency.
        if cost_eff > max_cost_eff:
            best_cost = name
            max_cost_eff = cost_eff

    # Print the best storage and cost efficiencies.

    load_results_animation()

    print(">Best can size in STORAGE efficiency:", best_store)
    time.sleep(1)
    print(">Best can size in COST efficiency   :", best_cost)
    time.sleep(1)

    # Finish message
    finish()


def compute_storage_efficiency(radius, height):
    """Compute and return the storage efficiency of a steel can size.
    The storage efficiency is the volume of the can divided by its
    surface area.

    Parameters
        radius: the radius of the steel can
        height: the height of the steel can
    Return: the storage efficiency of the steel can
    """
    volume = compute_volume(radius, height)
    surf_area = compute_surface_area(radius, height)
    efficiency = volume / surf_area
    return efficiency


def compute_cost_efficiency(radius, height, cost):
    """Compute and return the cost efficiency of a steel can size.
    The cost efficiency is the volume of the can divided by its cost.

    Parameters
        radius: the radius of the steel can
        height: the height of the steel can
        cost: the cost of the steel can
    Return: the cost efficiency of the steel can
    """
    volume = compute_volume(radius, height)
    efficiency = volume / cost
    return efficiency


def compute_volume(radius, height):
    """Compute and return the volume of a cylinder.

    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the volume of the cylinder
    """
    volume = math.pi * radius**2 * height
    return volume


def compute_surface_area(radius, height):
    """Compute and return the surface area of a cylinder.

    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the surface area of the cylinder
    """
    surf_area = 2 * math.pi * radius * (radius + height)
    return surf_area

def welcome():
    print("================================================")
    time.sleep(1)
    print("Welcome to the Can's Efficiency Comparator!")
    time.sleep(1)
    print("This program will help you calculate efficiency from values previously entered.")
    time.sleep(1)
    print("Let's get started!\n")
    time.sleep(1)

def finish():
    print("\nThank you for using the Can's Efficiency Comparator!")
    time.sleep(1)
    print("See you next time!")
    time.sleep(1)
    print("================================================")

def load_animation():
    animation = ["Calculating.","Calculating..","Calculating..."]
    for i in range(len(animation)):
        time.sleep(0.8)
        print("\r" + animation[i % len(animation)], end="")
    

def load_results_animation():
    print("\n >Now lets compare the results!<\n")
    time.sleep(1)
    animation = ["Calculating.","Calculating..","Calculating..."]
    for i in range(len(animation)):
        time.sleep(0.8)
        print("\r" + animation[i % len(animation)], end="")
    print("\n")


# Start this program by
# calling the main function.
main()
