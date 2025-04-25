def getnum(n):
    for i in range(n):
        yield i
a=getnum(5)

print(next(a))
print(next(a))
print(next(a))