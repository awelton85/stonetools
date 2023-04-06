import math
import sys

VALID_OPTIONS = (1, 2)


def get_option():
    option = input("Enter 1 for piece length or 2 for arc length: ")
    if option == "q":
        sys.exit()
    elif int(option) in VALID_OPTIONS:
        return int(option)
    else:
        print("Not a valid option.")
        return get_option()


def calculate_piece_length(overall_length, num_pieces, joint_spacing):
    return (overall_length - (num_pieces - 1) * joint_spacing) / num_pieces


def calculate_arc_length(radius, chord_length):
    return 2 * radius * math.asin(chord_length / (2 * radius))


def request_piece_length_inputs():
    overall_length = input("Enter the overall length in inches: ")
    if overall_length == "q":
        return None
    number_of_pieces = int(input("Enter the number of pieces: "))
    joint_spacing = float(input("Enter the joint spacing in decimal inches: "))
    return float(overall_length), number_of_pieces, joint_spacing


def request_arc_length_inputs():
    radius = input("Enter the radius in inches: ")
    if radius == "q":
        return None
    chord_length = float(input("Enter the chord length in inches: "))
    return float(radius), chord_length


def main():
    while True:
        option = get_option()

        if option == 1:
            inputs = request_piece_length_inputs()
            if inputs is not None:
                overall_length, num_pieces, joint_spacing = inputs
                result = calculate_piece_length(
                    overall_length, num_pieces, joint_spacing
                )
                print(f'Each piece length is {result}".\n')
        elif option == 2:
            inputs = request_arc_length_inputs()
            if inputs is not None:
                radius, chord_length = inputs
                result = calculate_arc_length(radius, chord_length)
                print(f'The arc length is {result}".\n')


if __name__ == "__main__":
    main()
