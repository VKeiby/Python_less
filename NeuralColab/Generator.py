def genf():
    for i in [23,42,14]:
        yield i

s = genf()
print(next(s))
print(next(s))
print(next(s))
# print(next(s)) #StopIteration

# ------------========----------

def fact(n):
    pr = 1
    for i in range (1,n+1):
        pr=pr*i
        yield pr

for i in fact(10):
    print(i,end=' ')