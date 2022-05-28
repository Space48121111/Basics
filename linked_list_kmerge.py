from __future__ import annotations

lists = [[1,4,5],[1,3,4],[2,6]]

'''
output = [1,1,2,3,4,4,5,6]
ascending order already k: len
algorithm/brutal force:
def bt(i, j): if ls[i][j] < ls[i][j + 1]:
    ls[i].next = ls[j].next bt(i + 1, j + 1)
Time complexity: O(nlogk)
go over every two nodes O(n),
then cmp depth reduce by two-fold every step /2 /(2 * 2):
2^t = k/len t = logk 2^3 = 8
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return 'Linked Node: val = ' + str(self.val) + \
        ', next = {' + str(self.next) + '}'
class Merge:
    def merged_lists(self, ls: List(ListNode(ListNode))) \
    -> Optional(ListNode):
        if not ls or len(ls) == 0:
            return None
        while len(ls) > 1:
            ml = []
            for i in range(0, len(ls), 2):
                l1 = ls[i]
                l2 = ls[i + 1] if (i + 1) < len(ls) else None
                ml.append(self.todo_list(l1, l2))
            ls = ml
            # print('New ls: ', ls[0])
        return ls[0]


    def todo_list(self, l1: ListNode, l2: ListNode):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        return dummy.next

def ls_to_ln(arr):
    if len(arr) < 1:
        return None
    elif len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next = ls_to_ln(arr[1:]))

res = []
for l in lists:
    ls = ls_to_ln(l)
    res.append(ls)
print(res)
m = Merge()
print(m.merged_lists(res))









# end
