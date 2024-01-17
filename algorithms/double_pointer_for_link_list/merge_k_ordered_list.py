# 合并k个有序链表

import heapq

from data_structures.list_node import ListNode
from data_structures.priority_queue import PriorityQueue


def mergeKList(a_list: list[ListNode]) -> ListNode:
    p = dummy = ListNode(0)
    # 优先级队列, 最小堆
    pq = PriorityQueue()
    for head in a_list:
        if head:
            pq.push(head, head.data)

    while pq.heap:
        # 获取最小节点, 接到结果链表中
        node = pq.pop()
        p.next = node
        if node.next:
            pq.push(node.next, node.next.data)
        p = p.next

    return dummy.next


if __name__ == '__main__':
    lists = [ListNode.fromList([1, 4, 5]), ListNode.fromList([1, 3, 4]), ListNode.fromList([2, 6])]
    reuslt = mergeKList(lists)
    print(reuslt.toString())