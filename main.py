def recursive_sum(data):
    total = 0
    if isinstance(data, dict):
        for value in data.values():
            total += recursive_sum(value)
    elif isinstance(data, list):
        for item in data:
            total += recursive_sum(item)
    elif isinstance(data, (int, float)):  # Check for numeric values
        total += data
    return total

# Example dictionary with nested structures
nested_dict = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3,
            'f': [4, 5, 6]
        }
    }
}

# Calculating the sum of all values
result = recursive_sum(nested_dict)
print(f'The sum of all values is: {result}')
