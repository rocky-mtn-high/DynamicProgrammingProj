#
# def max_wood(segments, i, j):
#     if i > j:
#         return 0
#     if i == j:
#         return segments[i]
#     left = segments[i] + max_wood(segments, i + 1, j)
#     right = segments[j] + max_wood(segments, i, j - 1)
#     return max(left, right)

def max_wood(segments, i, j):
    if i == j:
        return segments[i]
    total_left = sum(segments[i:j+1])
    return total_left - min(max_wood(segments, i + 1, j),max_wood(segments, i, j - 1) )

def max_wood_bu(segments):
    l = len(segments)
    ##max val is 1000, so initalize at 1001
    table = [[1001 for j in range(l)] for i in range(l)]

    ##base cases
    for i in range(l):
        for j in range(l):
            if i == j:
                table[i][j] = segments[i-1]

    ##now bottom up recurse
    ##do i + 1 = j, then i + 2 = j, ... along diagonals
    for i in range(0, n):

    return(table[0][l-1])
    ##sum of segments from i to j - min of recursive calls
