from collections import Counter

def first_most_occuring(s):
    freq=Counter(s)

    most_freq= max(freq, key=lambda  x: (freq[x], -s.index(x)))
    return most_freq

input="puppy"
result=first_most_occuring(input)
print(result)