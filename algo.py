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

def max_wood_traceback(segments):
    n = len(segments)
    dp = [[0] * n for _ in range(n)]
    parent = [[None] * n for _ in range(n)]

    segment_sums = [0] * (n + 1)
    for i in range(1, n + 1):
        segment_sums[i] = segment_sums[i - 1] + segments[i - 1]

    ##fill in segments
    for i in range(n):
        dp[i][i] = segments[i]
        parent[i][i] = 'S'
    ##compute table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            total_left = segment_sums[j + 1] - segment_sums[i]
            dp[i][j] = total_left - min(dp[i + 1][j], dp[i][j - 1])

            ##updating parent cells
            left = dp[i + 1][j]
            right = dp[i][j - 1]

            if left < right or  left == right: ##tiebreakjer
                dp[i][j] = total_left - left
                parent[i][j] = 'L'
            else:
                dp[i][j] = total_left - right
                parent[i][j] = 'R'

    ##Do traceback based on indices across table
    order = []
    i, j = 0, n - 1
    while i < j:
        if parent[i][j] == 'L':
            order.append(i)
            i += 1
        else: ##this is if parent = R
            order.append(j)
            j -= 1
    if i ==j:
        order.append(i)


    return dp[0][n - 1], [idx + 1 for idx in order]






