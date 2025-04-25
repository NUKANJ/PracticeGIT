def remove_duplicates(input_string):
    seen = set()
    result = []

    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

input_string = "aabbccddeeffgg"
output_string= remove_duplicates(input_string)

print("Original String:", input_string)
print("String without duplicates:", output_string)