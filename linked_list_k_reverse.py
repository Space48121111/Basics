from __future__ import annotations

head = [1,2,3,4,5]
k = 3

'''
output = [3,2,1,4,5]
algorithm/brutal force:
dummy group_prev w kth = get_k() group_next = kth.n
    w pre, curr = kth.n, group_prev.n
# shift k times and ret kth node
def get_k(curr, k) while c n k > 0: c = c.n k -= 1
'''

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    def __repr__(self):
        return 'List Node: val = ' + str(self.val) + \
        ', next = {' + str(self.next) + '}'

class kReverse:
    def k_group_nodes(self, h: Optional(ListNode), k: int) \
    -> Optional(ListNode):
        d = ListNode(0, h)
        gp = d
        while True:
            kt = self.get_k(gp, k)
            if not kt:
                break
            gn = kt.next

            # p, c = kt.next, gp.next
            p, c = gn, gp.next
            while c != gn:
                tmp1 = c.next
                c.next = p
                p = c
                c = tmp1
                # print('After ', p, c, c.next)
            tmp2 = gp.next
            gp.next = kt
            gp = tmp2
        return d.next
    def get_k(self, c: str, k: int) -> str:
        while c and k > 0:
            c = c.next
            k -= 1
        return c

def ls_to_ln(arr):
    if len(arr) < 1:
        return None
    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], ls_to_ln(arr[1:]))


ln = ls_to_ln(head)
kr = kReverse()
print(kr.k_group_nodes(ln, k))



# end
