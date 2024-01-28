# 删除有序数组中的重复项
from data_structures.list_node import ListNode


def remove_duplicates(arrays: list[int]) -> int:
    if len(arrays) == 0:
        return 0
    # 维护 nums[0...slow]
    slow = 0
    fast = 0
    while fast < len(arrays):
        if arrays[fast] != arrays[slow]:
            slow += 1
            # 维护 nums[0..slow] 无重复
            arrays[slow] = arrays[fast]
        fast += 1
    # 数组长度为索引 + 1
    return slow + 1


# 删除有序链表中的重复元素
def delete_duplicates_sorted_link(head):
    current = head

    while current is not None and current.next is not None:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head


# 删除链表中的重复元素
def remove_duplicates_link(linked_list: ListNode) -> ListNode:
    slow = linked_list
    fast = linked_list.next
    current = linked_list
    dummy = linked_list
    while current.next:
        while fast:
            if current.data == fast.data:
                slow.next = fast.next
            else:
                slow = fast
            fast = fast.next
        current = current.next
        slow = current
        fast = current.next

    return dummy


if __name__ == '__main__':
    a_list = [1, 2, 2]
    unsorted_nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 0, 2]
    sorted_nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # print(remove_duplicates(a_list))
    # print(remove_duplicates(sorted_nums))

    print(remove_duplicates_link(ListNode.fromList(unsorted_nums)).toString())
