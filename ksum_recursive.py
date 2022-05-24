from __future__ import annotations

input = [1,0,-1,0,-2,2]
target = 0
input1 = [2, 2, 2, 2]
target1 = 8
'''
output = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
unique quadruplets
algorithm/brutal force:
[-2. -1, 0, 0, 1, 2]
 a b l            r
4 a, b, l, r for i, b while l < r
if <: a += 1 l += 1 if >: r -=1
if f_s = tar: res.append(), a += 1 += 1
'''

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    res, quad = [], []
    nums.sort()
    def kSum(k: int, s: int, target: int):
        if k != 2:
            for i in range(s, len(nums) - k + 1):
                if i > s and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                quad.pop()
            return
        l, r = s, len(nums) - 1
        while l < r:
            t_s = nums[l] + nums[r]
            if t_s > target:
                r -= 1
            elif t_s < target:
                l += 1
            else:
                res.append(quad + [nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    kSum(4, 0, target)
    return res

print(fourSum(input1, target1))






# end
