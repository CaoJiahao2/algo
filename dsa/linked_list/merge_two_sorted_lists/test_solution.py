from dsa.linked_list.merge_two_sorted_lists.solution import ListNode, Solution

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

def test_merge():
    head = Solution().mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))
    assert to_list(head) == [1, 1, 2, 3, 4, 4]

