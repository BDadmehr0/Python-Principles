def zap(a, b):
    return [(a[i], b[i]) for i in range(len(a))]

# Example usage:
result = zap([0, 1, 2, 3], [5, 6, 7, 8])
print(result)

