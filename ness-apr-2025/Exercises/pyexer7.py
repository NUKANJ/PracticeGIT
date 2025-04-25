list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]

# Get odd-index elements from list1
odd_index_list1 = [list1[i] for i in range(1, len(list1), 2)]

# Get even-index elements from list2
even_index_list2 = [list2[i] for i in range(0, len(list2), 2)]

# Combine them into list3
list3 = odd_index_list1 + even_index_list2

# Print results
print("Element at odd-index positions from list one")
print(odd_index_list1)

print("Element at even-index positions from list two")
print(even_index_list2)

print("Printing Final third list", list3)
