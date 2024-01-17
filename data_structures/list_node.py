class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    @classmethod
    def fromList(cls, array: list):
        if not array:
            return None
        # 使用数组的第一个元素作为链表的头节点
        head = ListNode(array[0])
        current = head

        # 遍历数组的其余部分, 创建链表节点并🔗起来
        for value in array[1:]:
            current.next = ListNode(value)
            current = current.next

        return head

    def toString(self):
        if not self:
            return 'ListNode:null'
        current = self.next
        description = f'ListNode: {self.data}'
        while current:
            description = description + f' -> {current.data}'
            current = current.next
        return description

    def toList(self):
        if not self:
            return None
        a_list = []
        current = self
        while current:
            a_list.append(current.data)
            current = current.next

        return a_list
