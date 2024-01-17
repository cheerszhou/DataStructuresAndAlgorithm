# 快慢指针判断链表是否包含环
from data_structures.list_node import ListNode


def hasCycle(head: ListNode) -> bool:
    slow, fast = head, head

    # 快指针走到末尾时停止
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == '__main__':
    head = ListNode.fromList([2,3,-1,2])
    trail = head.trail()
    # trail.next = head
    print(trail.toList())