def perfect_number(n):
    if n<=0:
        return False

    sum_of_divisors = 0
    for i in range(1,n):
        if n%i == 0:
            sum_of_divisors+=i

    return sum_of_divisors == n

num =4
if perfect_number(num):
    print(f"{num} is perfect")
else:
    print(f"{num} is not perfect")