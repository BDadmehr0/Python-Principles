def consecutive_zeros(binary_string):
    max_zeros = 0
    current_zeros = 0

    for digit in binary_string:
        if digit == "0":
            current_zeros += 1
            max_zeros = max(max_zeros, current_zeros)
        else:
            current_zeros = 0

    return max_zeros

