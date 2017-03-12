import ast
import sys


def hell_triangle(triangle):
    try:
        return calculate_maximum_total(triangle)
    except IndexError:
        print("Invalid triangle input")


def calculate_maximum_total(triangle):
    index = max_index = total = 0
    # takes out the first row of the triangle and adds it to the total
    first_row = triangle.pop(0)
    total += first_row[0]
    for row in triangle:
        # decides what's the max element of the triangle and adds it to the total
        if row[index] > row[index + 1]:
            max_index = index
        else:
            max_index = index + 1
        total += row[max_index]
    return total


def main():
    # handles command line input converting it into a list
    triangle = ast.literal_eval(sys.argv[1])
    result = hell_triangle(triangle)
    print(result)

if __name__ == "__main__":
    main()
