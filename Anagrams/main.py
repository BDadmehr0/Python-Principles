def is_anagram(str1, str2):
    # Convert both strings to lowercase for case-insensitive comparison
    str1 = str1.lower()
    str2 = str2.lower()

    # Sort the characters in both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Compare the sorted strings
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False

