list_of_values = [5,12,172,19,25,35]

def fun(value):
    if value % 2 ==0:
        return True
    else:
        return False

even_list = filter(fun, list_of_values)

print(even_list)

for value in even_list:
    print(value)

v1 = (28,30,40)
v2 = list(v1)

print(v1)
print(v2)


def getlen(wd):
    return len(wd)

cities = ['chester','manchester','leichester','liverpool']
new_list = map(getlen,cities)

for x in new_list:
    print(x)