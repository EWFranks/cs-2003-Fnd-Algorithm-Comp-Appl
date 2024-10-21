def knapSack(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:

        return 0

    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if wt[n - 1] > W:

        return knapSack(W, wt, val, n - 1)


    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:


        return max(
            val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
            knapSack(W, wt, val, n - 1))


#print(val[3 - 1] + knapSack(11 - 5[3 - 1], 5, 18, 3 - 1),knapSack(11, 5, 18, 3 - 1)))


# Driver Code
val = [1, 6, 18]
wt = [1, 2, 5]
W = 8
n = len(val)
print(knapSack(W, wt, val, n))
print(W)
print(wt)
