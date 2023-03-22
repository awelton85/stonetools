import sys
import math

try:
    option = int(sys.argv[1])
except IndexError:
    print("No option selected.")
    sys.exit()

valid_options = [1, 2]


# calculates piece length after removing stonetools
def piece_length(oal, num_pieces, j_space):
    return (oal - (num_pieces - 1) * j_space) / num_pieces


# calculates arc length from radius and chord length
def arc_length(radius, chord_length):
    return 2 * radius * math.asin(chord_length / (2 * radius))


if option == 1:
    overall_length = float(input("Enter the overall length in inches: "))
    number_of_pieces = int(input("Enter the number of pieces: "))
    joint_spacing = float(input("Enter the joint spacing in decimal inches: "))
    print(
        f"The piece length is {piece_length(overall_length, number_of_pieces, joint_spacing)} inches."
    )

elif option == 2:
    rad = float(input("Enter the radius in inches: "))
    chord = float(input("Enter the chord length in inches: "))
    print(f"The arc length is {arc_length(rad, chord)} inches.")

elif option not in valid_options:
    print("Not a valid option.")
