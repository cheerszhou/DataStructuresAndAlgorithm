# 单链表的倒数第K个节点
from data_structures.list_node import ListNode


def findFromEnd(head: ListNode, k: int) -> ListNode:
    p1 = head
    # p1先走k步
    for i in range(k):
        p1 = p1.next

    p2 = head

    # p1 和 p2同时走 n - k 步
    while p1:
        p2 = p2.next
        p1 = p1.next

    # 现在p2指向第n-k+1个节点, 即倒数第k个节点
    return p2


# 删除链表的倒数第N个节点
def removeFromEnd(head: ListNode, n: int) -> ListNode:
    # 虚拟头结点
    dummy = ListNode(-1)
    dummy.next = head

    # 先找到链表倒数第n+1个节点, 才能删除倒数第n个节点
    target_node = findFromEnd(dummy, n + 1)

    # 删掉target_node的下一个节点
    target_node.next = target_node.next.next

    return dummy.next


if __name__ == '__main__':
    head = ListNode.fromList([1, 2, 3, 4, 5])
    n = 2
    print(removeFromEnd(head, n).toList())
