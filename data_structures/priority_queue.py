import heapq


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    # 每次返回优先级priority最小的item
    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        else:
            raise IndexError("该队列已清空")
