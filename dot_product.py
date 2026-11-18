def python_dot(left, right):
    total = 0
    for left_value, right_value in zip(left, right):
        total += left_value * right_value
    return total