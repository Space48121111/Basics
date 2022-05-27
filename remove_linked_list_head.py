from __future__ import annotations

input = [1,2,3,4,5]
n = 2
'''
output = [1,2,3,5]
algorithm/brutal force:
inp.remove(inp[n]) inp[:-n].pop()
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # nested dict of next {}
    def __repr__(self):
        return 'List Node: (val=' + str(self.val) + \
        ', next={' + str(self. next) + '})'
def remove(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    print(dummy)
    l = dummy
    r = head # + n in a loop as below
    while n > 0 and r:
        r = r.next
        n -= 1

    # shifting
    while r:
        l = l.next
        r = r.next

    # removing
    l.next = l.next.next
    return dummy.next

def list_to_ls_node(arr):
    if len(arr) < 1:
        return None
    elif len(arr) == 1:
        return ListNode(arr[0])
    # recursively nest/iterate over next from the first element/head
    return ListNode(arr[0], next=list_to_ls_node(arr[1:]))



ls = list_to_ls_node(input)
print(remove(ls, n))





# end
