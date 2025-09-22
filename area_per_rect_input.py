#!/usr/bin/env python3

# Created By: Nebiyu
# Date: September 22th, 2025
# This program displays the area and perimeter of a rectangle.

# Takes input from user
length = int(input("Enter length of the rectangle (cm): "))
width = int(input("Enter width of the rectangle (cm): "))


# Function to calculate the area and perimeter of a rectangle
def main():
    print("The Perimeter and Area of a Rectangle is:")
    print()
    print("The area is: {}cm^2".format(length * width))
    print("The perimeter is: {}cm".format(2 * (length + width)))


if __name__ == "__main__":
    main()
