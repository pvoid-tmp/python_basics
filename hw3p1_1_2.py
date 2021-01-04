from math import sqrt


# возвращает длину вектора, заданного списком (кортежем) координат
def magnitude(vector):
    mag = 0.0
    for c in vector:
        mag += float(c) ** 2
    return sqrt(mag)


def main():
    v1 = [10, 10, 10]
    v2 = [0, 0, -10]
    v3 = (10, 10, 0)

    print(magnitude(v1))
    print(magnitude(v2))
    print(magnitude(v3))
    input("\n Press Enter key to exit")


main()
