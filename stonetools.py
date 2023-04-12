import math
import sys


def request_float_input(prompt):
    while True:
        try:
            value = input(prompt)
            if value.lower() == "q":
                return None
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def request_int_input(prompt):
    while True:
        try:
            value = input(prompt)
            if value.lower() == "q":
                return None
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_option():
    valid_options = {1, 2}  # can be changed to omit options for testing

    while True:
        option = request_int_input("Enter 1 for piece length, 2 for arc length, or (q)uit: ")
        if option is None:
            sys.exit()

        if option in valid_options:
            return option
        else:
            print("Not a valid option.")


def calculate_piece_length(overall_length, num_pieces, joint_spacing):
    return (overall_length - (num_pieces - 1) * joint_spacing) / num_pieces


def calculate_arc_length(radius, chord_length):
    return 2 * radius * math.asin(chord_length / (2 * radius))


def request_piece_length_inputs():
    overall_length = request_float_input("Enter the overall length in inches, or (q)uit: ")
    if overall_length is None:
        return None

    number_of_pieces = request_int_input("Enter the number of pieces, or (q)uit: ")
    if number_of_pieces is None:
        return None

    joint_spacing = request_float_input("Enter the joint spacing in decimal inches, or (q)uit: ")
    if joint_spacing is None:
        return None

    return overall_length, number_of_pieces, joint_spacing


def request_arc_length_inputs():
    radius = request_float_input("Enter the radius in inches, or (q)uit: ")
    if radius is None:
        return None

    chord_length = request_float_input("Enter the chord length in inches, or (q)uit: ")
    if chord_length is None:
        return None

    return radius, chord_length


def main():
    while True:
        option = get_option()

        if option == 1:
            inputs = request_piece_length_inputs()
            if inputs is not None:
                overall_length, num_pieces, joint_spacing = inputs
                result = calculate_piece_length(overall_length, num_pieces, joint_spacing)
                print(f'Each piece length is {result}".\n')
        elif option == 2:
            inputs = request_arc_length_inputs()
            if inputs is not None:
                radius, chord_length = inputs
                result = calculate_arc_length(radius, chord_length)
                print(f'The arc length is {result}".\n')


if __name__ == "__main__":
    main()
