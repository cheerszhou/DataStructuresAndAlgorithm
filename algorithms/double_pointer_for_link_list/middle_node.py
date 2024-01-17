# 快慢指针寻找单链表的中点
from data_structures.list_node import ListNode


def middleNode(head: ListNode) -> ListNode:
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


if __name__ == '__main__':
    print(middleNode(ListNode.fromList([12, 3, 3, 5, 6, 7, 2, 3])).data)
