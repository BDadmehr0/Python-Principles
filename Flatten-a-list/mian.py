def flatten(lst):
    flattened = []
    for sublist in lst:
        flattened.extend(sublist)
    return flattened

# Example usage:
result = flatten([[1, 2], [3, 4]])
print(result)

