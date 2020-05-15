def diagonalDifference(arr):
    # Write your code here

    # based on the length, we will know how many elements to pick
    # for calculating diagonals

    num_of_elements = len(arr)

    # Now select the appropriate elements each diagonal

    first_diag = []
    for i in range(num_of_elements):
        first_diag.append(arr[i][i])
    second_diag = []
    for j in range(num_of_elements):
        second_diag.append(arr[num_of_elements-j-1][j])

    return abs(sum(first_diag)-sum(second_diag))
