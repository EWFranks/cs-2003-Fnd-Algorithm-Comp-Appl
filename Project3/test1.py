n=6     #2D array
m=12
a=[]

a=[[i * j for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        print('{:3d}'.format(a[i][j]),end=" ")
    print()
print()
