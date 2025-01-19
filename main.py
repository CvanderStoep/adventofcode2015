def contains_two_different_pairs(s):
    pairs = set()
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            pairs.add(s[i])
            i += 2  # Move past the current pair
        else:
            i += 1

    return len(pairs) >= 2


# Example usage:
example_string = "aabb"
result = contains_two_different_pairs(example_string)
print(result)  # Output: True

example_string = "abcde"
result = contains_two_different_pairs(example_string)
print(result)  # Output: False

example_string = "bookkeeper"
result = contains_two_different_pairs(example_string)
print(result)  # Output: True
