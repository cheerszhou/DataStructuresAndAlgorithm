# 合并两个有序的链表
from data_structures.list_node import ListNode


def mergeTwoList(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    p = dummy
    p1 = l1
    p2 = l2

    while p1 and p2:
        # 比较p1和p2两个指针, 将值较小的节点接到p指针
        if p1.data > p2.data:
            p.next = p2
            p2 = p2.next
        else:
            p.next = p1
            p1 = p1.next
        # p 指针不断前进
        p = p.next

    if p1:
        p.next = p1

    if p2:
        p.next = p2

    return dummy.next


if __name__ == '__main__':
    ordered_l1 = ListNode.fromList([-1, 2, 4])
    ordered_l2 = ListNode.fromList([1, 13, 20])
    ordered_l = mergeTwoList(ordered_l1, ordered_l2)
    print(ordered_l.toString())
    print(ordered_l.toList())
