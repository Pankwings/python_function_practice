from math import pi 
def circle_area(radius):
    if type(radius) not in [int ,float]:
        raise TypeError("The radius must be non-negative real number")
    if radius < 0:
        raise ValueError("The radius of a circle cannot be negative.")
    area = radius*radius*pi
    print(area)
    return(area)   

#
#r = [2, 4, -1, True, 'Hello']
#message = "The area of circle having radius {radius} is {area}."
#for radius in r:
#    area = circle_area(radius)
#    print(message.format(radius = radius,area=area))    

