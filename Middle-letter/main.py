def mid(string):
    length = len(string)
    if length % 2 == 0:  # Even-length string
        return ""
    else:  # Odd-length string
        middle_index = length // 2
        return string[middle_index]

