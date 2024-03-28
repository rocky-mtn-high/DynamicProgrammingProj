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

    ##sum of segments from i to j - min of recursive calls
