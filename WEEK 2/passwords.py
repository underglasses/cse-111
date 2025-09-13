"""
"""
import math

#volume = π radius2 height
#surface_area = 2π radius (radius + height)

def main():
    print(f'#1 Picnic {storage_efficiency(6.83,10.16)}')
    print(f'#1 Tall {storage_efficiency(7.78,11.91)}')
    print(f'#2 {storage_efficiency(8.73,11.59)}')
    print(f'#2.5 {storage_efficiency(10.32,11.91)}')
    print(f'#3 Cylinder {storage_efficiency(10.79,17.78)}')
    print(f'#5 {storage_efficiency(13.02,14.29)}')
    print(f'#6Z {storage_efficiency(5.40,8.89)}')
    print(f'#8Z short {storage_efficiency(6.83,7.62)}')
    print(f'#10 {storage_efficiency(15.72,17.78)}')
    print(f'#211 {storage_efficiency(6.83,12.38)}')
    print(f'#300 {storage_efficiency(7.62,11.27)}')
    print(f'#303 {storage_efficiency(8.10,11.11)}')


def compute_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

def compute_surface_area(radius, height):
    area = 2 * math.pi * radius * (radius + height)
    return area

def storage_efficiency(radius, height):
    storage = round(compute_volume(radius, height) / compute_surface_area(radius, height), 2)
    return storage


main()