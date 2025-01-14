# Function to calculate the encoded length of the string
def encoded_length(line):
    encoded_string = '"'  # Start with an extra double quote
    for char in line:
        if char == '\\' or char == '"':
            encoded_string += '\\'  # Add an escape character for backslash or double quote
        encoded_string += char
    encoded_string += '"'  # End with an extra double quote
    return len(encoded_string)

# Read the file containing the string literals
with open('input\input8.txt', 'r') as file:
    lines = file.readlines()

total_encoded_length = 0
total_original_length = 0

# Iterate over each line and calculate the totals
for line in lines:
    line = line.strip()
    total_original_length += len(line)
    total_encoded_length += encoded_length(line)

# Calculate the difference
difference = total_encoded_length - total_original_length

print(f'Total encoded length: {total_encoded_length}')
print(f'Total original length: {total_original_length}')
print(f'Difference: {difference}')
