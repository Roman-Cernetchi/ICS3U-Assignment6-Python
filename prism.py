#!/usr/bin/env python3

# Created by: Roman Cernetchi
# Created on: January 2021
# This program calculates the volume of a cylinder

import math


def calculate_surface_area(length, width, height):
    # calculates the surface area of rectangular prism

    surface_area = (width*length+height*length+height*width)*2
    float_area = "{:.2f}".format(surface_area)

    return float_area


def main():
    # input the length, width, and height
    while True:
        try:
            user_length = float(input("Enter the length of the"
                                      " rectangular prism(cm): "))
            user_width = float(input("Enter the width of the"
                                     " rectangular prism(cm): "))
            user_height = float(input("Enter the height of the"
                                      " rectangular prism(cm): "))
            print("")

            # calls function
            float_area = calculate_surface_area(user_length, user_width,
                                                user_height)

            if user_length <= 0 or user_width <= 0 or user_height <= 0:
                print("Invalid input")
            else:
                # output
                print("The surface area is: {0} cm²".format(float_area))
                break

        except ValueError:
            print("This was not a number")


if __name__ == "__main__":
    main()
