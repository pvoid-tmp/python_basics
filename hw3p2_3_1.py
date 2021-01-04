import numpy as np


def polar_to_cartesian(radius, azimuth):
    return radius * np.cos(azimuth), radius * np.sin(azimuth)


def main():
    while True:
        if (r := input("Radius (Q for quit): ")).upper() == 'Q':
            break
        try:
            a = float(input("Azimuth in radians: "))
            x = polar_to_cartesian(float(r), a)
            print(f"x = {x[0]:.6f}, y = {x[1]:.6f}\n")
        except Exception as e:
            print(e)


main()
