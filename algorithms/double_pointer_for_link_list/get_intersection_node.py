# 两个链表是否相交
from data_structures.list_node import ListNode


def getIntersectionNode1(headA: ListNode, headB: ListNode) -> ListNode:
    # p1 指向 A 链表头结点, p2 指向 B 链表头结点
    p1, p2 = headA, headB
    while p1 != p2:
        # p1 走一步, 如果走到 A 链表末尾, 转到 B 链表
        if p1 is None:
            p1 = headB
        else:
            p1 = p1.next
        # p2 走一步, 如果走到 B 链表末尾, 转到 A 链表
        if p2 is None:
            p2 = headA
        else:
            p2 = p2.next
    return p1


def getIntersectionNode2(headA: ListNode, headB: ListNode) -> ListNode:
    lenA, lenB = 0, 0
    # 计算两条链表的长度
    p1, p2 = headA, headB
    while p1:
        lenA += 1
        p1 = p1.next
    while p2:
        lenB += 1
        p2 = p2.next

    # 让
