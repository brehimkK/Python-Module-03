#!/usr/bin/env python3


import math


def calculate_distance(p1: tuple, p2: tuple) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    nb = (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2
    return math.sqrt(nb)


def parse_coordinates(inputs: str) -> tuple:
    original = inputs
    inputs = inputs.split(',')
    numbers = []
    if len(inputs) != 3:
        return None
    try:
        for i in range(len(inputs)):
            numbers.append(int(inputs[i]))
    except ValueError as a:
        print(f'Parsing invalid coordinates: "{original}"')
        print(f'Error parsing coordinates: {a}')
        print(f'Error details - Type: {type(a).__name__}, Args: {a.args}')
        return None

    return tuple(numbers)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    origin = (0, 0, 0)
    p1 = (10, 20, 5)
    print(f"\nPosition created: {p1}")
    dist1 = calculate_distance(origin, p1)
    print(f"Distance between {origin} and {p1}: {dist1:.2f}")

    g = "3,4,0"
    dest2 = parse_coordinates(g)

    g = "3,4,0"
    print(f'\nParsing coordinates: "{g}"')
    p2 = parse_coordinates(g)
    print(f"Parsed position: {p2}")
    dist2 = calculate_distance(origin, p2)
    print(f"Distance between {origin} and {p2}: {dist2:.1f}\n")

    parse_coordinates("abc,def,ghi")

    print("\nUnpacking demonstration:")
    x, y, z = p2
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
