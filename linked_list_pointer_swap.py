from __future__ import annotations

head = [1,2,3,4]

'''
output = [2,1,4,3] use pointer, not val!
algorithm/brutal force: # visual
dummy for i in l:
    l[i].next = l[i + 1] l[i + 1].next = l[i] break
    ret dummy.next
'''

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    def __repr__(self):
        return 'List Node: val = ' + str(self.val) + \
        ', next = {' + str(self.next) + '}'

def swap(h: Optional(ListNode)) -> Optional(ListNode):
    d = ListNode(0, h)
    p, c = d, h
    while c and c.next:
        np = c.next.next
        s = c.next

        s.next = c
        c.next = np
        p.next = s

        p = c
        c = np
    return d.next

def ls_to_ln(arr):
    if len(arr) < 1:
        return None
    elif len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], ls_to_ln(arr[1:]))


ls = ls_to_ln(head)
print(swap(ls))








# end
