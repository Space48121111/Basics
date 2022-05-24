from __future__ import annotations

input = [-1,2,1,-4]

'''
target = 1
output = 2 -1 + 2 + 1 # -4 1 2 -1 2

algorithm/brutal force:
sort() for i, a if a == n[i -1] l, r i + 1, len(n) - 1
if == tar: ret elif > else < min(abs(tar - t_sum), abs(tar - min_s))
while n[l] == n[l - 1] l += 1
'''

def ThreeSumClosest(nums: List[int], target: int) -> int:
    min_s = -999999
    nums = sorted(nums)
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            t_sum = a + nums[l] + nums[r]
            if t_sum == target:
                return t_sum
            # tar = 1 -1 2 1 2 -> 1 # -4 1 2 -1 -> 2
            elif abs(target - min_s) > abs(target - t_sum):
                min_s = t_sum
            elif t_sum < target:
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
            else:
                r -= 1

    return min_s


print(ThreeSumClosest(input, 1))







# end
