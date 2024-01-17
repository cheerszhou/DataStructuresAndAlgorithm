from data_structures.node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    # 在链表尾部插入元素
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        # 找到末尾, 并在末尾插入新节点
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # 在链表头部插入元素
    def prepend(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    # 删除节点
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
            # 寻找值为data的节点
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next:
            current_node.next = current_node.next.next

    def __str__(self):
        if not self.head:
            return ""
        current_node = self.head.next
        display = f"{self.head.data}"
        while current_node:
            display = display + f" -> {current_node.data}"
            current_node = current_node.next
        return display
