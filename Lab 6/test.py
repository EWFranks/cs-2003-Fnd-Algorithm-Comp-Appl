count = 0
def justdoit(n):
    if n <= 1:
        return n
    else:
        if n == 3:
            count+1
        return (justdoit(n - 1) + justdoit(n - 2))


print(justdoit(5))
print(count)