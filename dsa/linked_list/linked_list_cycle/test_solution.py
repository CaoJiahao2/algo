from dsa.linked_list.linked_list_cycle.solution import ListNode, Solution

def test_has_cycle_true():
    a, b, c = ListNode(3), ListNode(2), ListNode(0)
    a.next = b
    b.next = c
    c.next = b
    assert Solution().hasCycle(a) is True

def test_has_cycle_false():
    a, b = ListNode(1), ListNode(2)
    a.next = b
    assert Solution().hasCycle(a) is False

