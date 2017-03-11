def hell_triangle(triangle):
    try:
        return calculate_maximum_total(triangle)
    except IndexError:
        print("Invalid triangle input")


def calculate_maximum_total(triangle):
    index = max_index = total = 0
    first_row = triangle.pop(0)
    total += first_row[0]
    for row in triangle:
        if row[index] > row[index + 1]:
            max_index = index
        else:
            max_index = index + 1
        total += row[max_index]
    return total


def main():
    print(hell_triangle([[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]]))


main()
