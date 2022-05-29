nums = [1, 1, 2]
nums1 = [0,0,1,1,1,2,2,3,3,4]

'''
output = 2, [1, 2, _] in-place slot O(1) space non-decreasing order
output1 = 5, [0,1,2,3,4,_,_,_,_,_]
algorithm/brutal force:
if n[i] = n[i - 1]: pop(n[i]) n_s.append(_)

'''

def unique(n):
    l = 1
    for r in range(1, len(n)):
        if n[r] != n[r - 1]:
            n[l] = n[r]
            l += 1
    return l, n

print(unique(nums1))










# end
