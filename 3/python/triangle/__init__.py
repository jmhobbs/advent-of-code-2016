def is_possible_triangle(a, b, c):
    largest = max(a, max(b, c))

    remaining = [a, b, c]
    remaining.remove(largest)

    return remaining[0] + remaining[1] > largest
