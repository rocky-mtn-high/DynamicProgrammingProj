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
##O(n^2)
def max_wood_bu(segments):
    n = len(segments)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = segments[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            total_left = sum(segments[i:j+1])
            dp[i][j] = total_left - min(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]
    ##sum of segments from i to j - min of recursive calls


