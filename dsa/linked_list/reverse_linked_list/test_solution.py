from dsa.linked_list.reverse_linked_list.solution import ListNode, Solution

def build(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def test_reverse():
    assert to_list(Solution().reverseList(build([1, 2, 3]))) == [3, 2, 1]

def test_reverse_empty():
    assert Solution().reverseList(None) is None

