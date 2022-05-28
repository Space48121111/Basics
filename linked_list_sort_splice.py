from __future__ import annotations

list1 = [1,2,4]
list2 = [1,3,4]

'''
output = [1,1,2,3,4,4]
algorithm/brutal force
cmp for i in l1: f j in l2: if l2[j] <= l1[i] < l2[j + 1]:
    res.append l2.next = l1.next ret res
'''

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return 'List Node: val = ' + str(self.val) + ', next = {' + \
        str(self.next) + '}'

def merge_sort(l1: Optional(ListNode), l2: Optional(ListNode)) \
    -> Optional(ListNode):
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

def list_to_ls_node(arr):
    if len(arr) < 1:
        return None
    elif len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next = list_to_ls_node(arr[1:]))

ls1 = list_to_ls_node(list1)
ls2 = list_to_ls_node(list2)
print(merge_sort(ls1, ls2))










# end
