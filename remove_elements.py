nums = [3,2,2,3]
val = 3

nums1 = [0,1,2,2,3,0,4,2]
val1 = 2
'''
output = 2, [2,2,_,_]
output1 = 5, [0,1,4,0,3,_,_,_]
algorithm/brutal force:
l = 1 for r in len(n): if n[r] != val: n[l] = n[r] r += 1
'''

def pointer(n, v):
    l = 0
    for r in range(len(n)):
        if n[r] != v:
            n[l] = n[r]
            l += 1

    return l

print(pointer(nums1, val1))





# end
