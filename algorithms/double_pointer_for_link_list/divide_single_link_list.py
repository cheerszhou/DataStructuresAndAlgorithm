# 单链表分解
import queue

from data_structures.list_node import ListNode


def partition(alist: ListNode, x: int) -> ListNode:
    p = alist
    p1 = dummy1 = ListNode(-1)
    p2 = dummy2 = ListNode(-1)
    while p:
        if p.data < x:
            p1.next = p
            p1 = p1.next
        else:
            p2.next = p
            p2 = p2.next
        temp = p.next
        p.next = None
        p = temp

    p1.next = dummy2.next
    return dummy1.next


if __name__ == '__main__':
    alist = ListNode.fromList([1, 4, 3, 2, 5, 2])
    result = partition(alist, 3)
    print(result.toString())
    divide = 2
    print('absefwef' if 4 / divide == 1 else 'mamma')
