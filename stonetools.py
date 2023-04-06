import math
import sys

valid_options = [1, 2]


def get_option():
    option = input("Enter 1 for piece length or 2 for arc length: ")
    if option == "q":
        sys.exit()
    elif int(option) in valid_options:
        return option
    else:
        print("Not a valid option.")
        get_option()


def piece_length(oal, num_pieces, j_space):
    """Calculates the piece length from the overall length, number of pieces, and joint spacing."""
    return (oal - (num_pieces - 1) * j_space) / num_pieces


def arc_length(radius, chord_length):
    """Calculates the arc length from the radius and chord length."""
    return 2 * radius * math.asin(chord_length / (2 * radius))


def overall_len():
    overall_length = float(input("Enter the overall length in inches: "))
    number_of_pieces = int(input("Enter the number of pieces: "))
    joint_spacing = float(input("Enter the joint spacing in decimal inches: "))

    print(
        f'Each piece length is {piece_length(overall_length, number_of_pieces, joint_spacing)}".'
    )
    overall_len()


def arc_len():
    rad = float(input("Enter the radius in inches: "))
    chord = float(input("Enter the chord length in inches: "))

    print(f'The arc length is {arc_length(rad, chord)}".')
    arc_len()


def main():
    option = get_option()
    if int(option) == 1:
        overall_len()
    elif int(option) == 2:
        arc_len()


if __name__ == "__main__":
    main()
