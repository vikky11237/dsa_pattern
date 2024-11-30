
def prefix_sum(arr, i, j):
    """
    Calculates the prefix sum of the given array between the
    given indices i and j.
    """
    print(arr)
    prefix_sum = []
    current_sum=0
    for num in arr:
        current_sum=current_sum+num
        prefix_sum.append(current_sum)
    if i==0:
        return prefix_sum,prefix_sum[j]
    else:
        return prefix_sum,prefix_sum[j]-prefix_sum[i-1]
    



