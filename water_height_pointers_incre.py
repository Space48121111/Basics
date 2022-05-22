from __future__ import annotations

input = ''' \
height = [1,8,6,2,5,4,8,3,7]
'''

'''
output = 49 max area no slanting/obliquing
sum([1:n - 1] * h[n - 1])
time complexity: O(n^2)
space complexity: O(1)
algorithm/brutal force:
    area = (j - i) * h[min(i, j)]
    max_a = max(max_a, area)
sliding window:
    bucket={}
    if not > bucket:
        bucket.append(max)
        i += 1
        j -= 1
'''

def maxArea(h: List[int]) -> int:
    max_a = 0  # float('-inf')
    l, r = 0, len(h) - 1
    while l < r:
        max_a = max(max_a, (r - l) * min(h[l], h[r]))
        print(min(h[l], h[r]))
        if h[l] < h[r]:
            l += 1
        else:
            r -= 1
    return max_a

print(maxArea([1,8,6,2,5,4,8,3,7]))


# end
