def knapSack(W, wt, val):
    n = len(val)
    data = [[i * j for j in range(W)] for i in range(n)]

    for i in range(n):
        for j in range(W):

            if i == 0 or j == 0:
                data[i][j] = 0
                print('{:3d}'.format(data[i][j]), end=" ")
            elif wt[i - 1] <= j:
                data[i][j] = max(val[i - 1]
                                 + data[i - 1][j - wt[i - 1]], data[i - 1][j])
                print('{:3d}'.format(data[i][j]), end=" ")

            else:
                data[i][j] = data[i - 1][j]
                print('{:3d}'.format(data[i][j]), end=" ")
        print("\n")


def main():
    val = [1, 6, 18, 21, 25]
    wt = [1, 2, 5, 6, 7]
    W = 20

    print(knapSack(W, wt, val))


main()
