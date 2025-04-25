first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [64, 49, 36, 25, 16, 9, 4]

# Create a set of pairs based on matching values
result_set = set()

# Loop through first_list and check if the element exists in second_list
for num in first_list:
    if num in second_list:
        result_set.add((num, num ** 2))

# Print the result
print("Result is", result_set)
