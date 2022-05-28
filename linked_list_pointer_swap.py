from __future__ import annotations

head = [1,2,3,4]

'''
output = [2,1,4,3] use pointer, not val!
algorithm/brutal force: # visual
dummy prev, curr, next_pair = c.n.n second = c.n
s.n = c p.n = s p = c c = np ret dummy.next
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
