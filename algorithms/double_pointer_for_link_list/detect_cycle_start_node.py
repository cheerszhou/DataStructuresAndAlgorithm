# 判断链表是否含环并判断起点
from data_structures.list_node import ListNode


def detectCycleStartNode(head: ListNode):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    if not fast or not fast.next:
        return None

    slow = head
    while slow != fast:
        fast = fast.next
        slow = slow.next
    return slow
