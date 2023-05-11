"""
This module contains functions for calculating the length of each piece of a
stone slab given the overall length, number of pieces, and joint spacing, as
well as the arc length and chord length of a circular arc given the radius and
either the arc length or chord length.
Updated for python 3.10.11 on 2023-05-11
"""
import math
import sys


# Input request and validation functions
def request_float_input(prompt: str) -> float | None:
    """Request a float input from the user."""
    while True:
        try:
            value = input(prompt)
            if value.lower() == "q":
                return None
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def request_int_input(prompt: str) -> int | None:
    """Request an integer input from the user."""
    while True:
        try:
            value = input(prompt)
            if value.lower() == "q":
                return None
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# Calculation functions
def calculate_piece_length(overall_length: float, num_pieces: int, joint_spacing: float) -> float:
    """Calculate the length of each piece given the overall length, number of pieces, and joint spacing."""
    return (overall_length - (num_pieces - 1) * joint_spacing) / num_pieces


def calculate_arc_length(radius: float, chord_length: float) -> float:
    """Calculate the arc length given the radius and chord length."""
    return 2 * radius * math.asin(chord_length / (2 * radius))


def calculate_chord_length(radius: float, arc_length: float) -> float:
    """Calculate the chord length given the radius and arc length."""
    return 2 * radius * math.sin(arc_length / (2 * radius))


# Input request functions
def request_piece_length_inputs() -> tuple[float, int, float] | None:
    """Request the overall length, number of pieces, and joint spacing from the user."""
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


def request_arc_length_inputs() -> tuple[float, float] | None:
    """Request the radius and chord length from the user."""
    radius = request_float_input("Enter the radius in inches, or (q)uit: ")
    if radius is None:
        return None

    chord_length = request_float_input("Enter the chord length in inches, or (q)uit: ")
    if chord_length is None:
        return None

    return radius, chord_length


def request_chord_length_inputs() -> tuple[float, float] | None:
    """Request the radius and arc length from the user."""
    radius = request_float_input("Enter the radius in inches, or (q)uit: ")
    if radius is None:
        return None

    arc_length = request_float_input("Enter the arc length in inches, or (q)uit: ")
    if arc_length is None:
        return None

    return radius, arc_length


def request_option() -> int:
    """Request the user to select an option from the menu."""
    valid_options = {1, 2, 3}  # can be changed to omit options for testing

    while True:
        option = request_int_input("Enter 1 for piece length, 2 for arc length, 3 for chord length or (q)uit: ")
        if option is None:
            sys.exit()

        if option in valid_options:
            return option
        else:
            print("Not a valid option.")


def main():
    while True:
        option = request_option()

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
        elif option == 3:
            inputs = request_chord_length_inputs()
            if inputs is not None:
                radius, arc_length = inputs
                result = calculate_chord_length(radius, arc_length)
                print(f'The chord length is {result}".\n')


if __name__ == "__main__":
    main()
