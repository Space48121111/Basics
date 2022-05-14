from __future__ import annotations

input = ''' \
nums1 = [1, 3, 4]
nums2 = [2]
'''
'''
output = 2.50000

algorithm: binary search
time complexity: O(log(m + n))
'''

# O(n + m)
def brutal_force(nums1: List(int), nums2: List(int)) -> float:
    list = sorted(nums1 + nums2)
    i = len(list) // 2
    if len(list) % 2:
        return list[i]
    else:
        return (list[i - 1] + list[i]) / 2


# O(log(min(m, n)))
def log(nums1: List(int), nums2: List(int)) -> float:
    a, b = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2
    print(half)
    if len(a) > len(b):
        a, b = b, a
    l, r = -1, len(a)
    while True:
        i = (l + r) // 2
        j = half - i - 2
        print(i, j)
        a_l = a[i] if i >= 0 else float('-infinity')
        a_r = a[i + 1] if (i + 1) < len(a) else float('infinity')
        print('a_l r', a_l, a_r)
        b_l = b[j] if j >= 0 else float('-infinity')
        b_r = b[j + 1] if (j + 1) < len(b) else float('infinity')
        print('b_l r', b_l, b_r)
        if a_l <= b_r and b_l <= a_r:
            if total % 2:
                return min(a_r, b_r)
            return (max(a_l, b_l) + min(a_r, b_r)) / 2
        elif a_l > b_r:
            r = i - 1
        else:
            l = i + 1

print(log([1, 2], [3, 4, 5]))
# print(brutal_force([1, 3, 4], [2]))





# end
