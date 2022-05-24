from __future__ import annotations

input = [-1,0,1,2,-1,-4]

'''
output = [[-1,-1,2],[-1,0,1]] no dup
algorithm/brutal force:
for [i, j, k] in inp:
    if i != j and j != k and k != i:
        if sum(i, j, k) == 0:
            return list([i, j, k])
'''

def ThreeSum(nums: List[int]) -> List[int]:
    res = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            three_sum = a + nums[l] + nums[r]
            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                # [-2, -2, 0, 0, 2, 2]
                while nums[l] == nums[l - 1]  and l < r:
                    l += 1
    return res
print(ThreeSum(input))















# end
