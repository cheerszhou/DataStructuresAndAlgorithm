# 两个链表是否相交
from data_structures.list_node import ListNode


def getIntersectionNode1(headA: ListNode, headB: ListNode) -> ListNode:
    # p1 指向 A 链表头结点, p2 指向 B 链表头结点
    p1, p2 = headA, headB
    while p1 and p2 and p1.data != p2.data:
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

    # 让 p1和p2到达尾不得距离相等
    p1, p2 = headA, headB
    if lenA > lenB:
        for i in range(lenA - lenB):
            p1 = p1.next
    else:
        for i in range(lenB - lenA):
            p2 = p2.next
    # 看两个指针是否相等, p1 == p2 时有两种情况:
    # 1 要么是两条链表不相交, 它们同时走到尾部空指针
    # 2 要么是两条链表相交, 它们走到两条链表的相交点
    while p1 and p2 and p1.data != p2.data:
        p1 = p1.next
        p2 = p2.next

    return p1


if __name__ == '__main__':
    aList1 = [0, 9, 1, 2, 5]
    aList2 = [3, 2, 4]
    print(getIntersectionNode1(ListNode.fromList(aList1), ListNode.fromList(aList2)).data)
    print(getIntersectionNode2(ListNode.fromList(aList1), ListNode.fromList(aList2)).data)
