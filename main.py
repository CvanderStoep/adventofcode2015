def count_non_overlapping_combinations(s):
    combinations = {}
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            combination = s[i] * 2
            if combination in combinations:
                combinations[combination] += 1
            else:
                combinations[combination] = 1
            i += 2  # Skip the next character to prevent overlap
        else:
            i += 1
    return combinations

# Example usage
input_string = "aaaabbbcccaaa"
result = count_non_overlapping_combinations(input_string)
print("Non-overlapping combination counts:", result)
