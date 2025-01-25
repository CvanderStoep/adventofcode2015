def fill_container(containers: list, liters: int) -> list:
    def find_combinations(containers, target, current_combination=None, all_combinations=None):
        if current_combination is None:
            current_combination = []
        if all_combinations is None:
            all_combinations = []

        if target == 0:
            all_combinations.append(current_combination.copy())
            return all_combinations

        if target < 0 or not containers:
            return all_combinations

        for i in range(len(containers)):
            current_combination.append(containers[i])
            find_combinations(containers[i+1:], target - containers[i], current_combination, all_combinations)
            current_combination.pop()

        return all_combinations

    return find_combinations(containers, liters)

# Example usage
containers = [20, 15, 10, 5, 5]
liters = 25

# Find all combinations
combinations_found = fill_container(containers, liters)

# Print the combinations found
print("Combinations:")
for combo in combinations_found:
    print(combo)

# Output the number of combinations found
print(f"Total combinations: {len(combinations_found)}")
