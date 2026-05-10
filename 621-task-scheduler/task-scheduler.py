class MaxHeap:
    def __init__(self):
        self.heap_arr = [-1]   # 1-indexed
        self.size = 0

    def heapify(self, arr):
        # TC: O(n) | SC: O(n)
        self.heap_arr = [-1] + arr
        self.size = len(arr)
        n = self.size
        for i in range(n // 2, 0, -1):
            curr = i
            while True:
                largest = curr
                left = 2 * curr
                right = 2 * curr + 1

                if left < n and self.heap_arr[largest] < self.heap_arr[left]:
                    largest = left
                if right < n and self.heap_arr[largest] < self.heap_arr[right]:
                    largest = right

                if curr == largest:
                    break

                self.heap_arr[largest], self.heap_arr[curr] = self.heap_arr[curr], self.heap_arr[largest]
                curr = largest

    def heappush(self, val):
        # TC: O(log n) | SC: O(1)
        self.size += 1
        self.heap_arr.append(val)
        current_idx = self.size
        parent_idx = current_idx // 2
        # Sift up: swap with parent while larger than parent
        while parent_idx > 0 and self.heap_arr[parent_idx] < self.heap_arr[current_idx]:
            self.heap_arr[current_idx], self.heap_arr[parent_idx] = self.heap_arr[parent_idx], self.heap_arr[current_idx]
            current_idx = parent_idx
            parent_idx = current_idx // 2

    def heappop(self):
        # TC: O(log n) | SC: O(1)
        n = self.size
        self.heap_arr[1], self.heap_arr[n] = self.heap_arr[n], self.heap_arr[1]
        pop_value = self.heap_arr.pop()
        self.size -= 1
        n -= 1

        parent_idx = 1
        while True:
            smallest = parent_idx  # candidate for swap
            left = parent_idx * 2
            right = parent_idx * 2 + 1

            if left <= n and self.heap_arr[smallest] < self.heap_arr[left]:
                smallest = left
            if right <= n and self.heap_arr[smallest] < self.heap_arr[right]:
                smallest = right

            if parent_idx == smallest:
                break

            self.heap_arr[parent_idx], self.heap_arr[smallest] = self.heap_arr[smallest], self.heap_arr[parent_idx]
            parent_idx = smallest

        return pop_value


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = MaxHeap()
        unique_tasks = set(tasks)
        unique_tasks_len = len(unique_tasks)
        circle_length = n + 1
        hm = {}
        intervals = 0
        for task in tasks:
            hm[task] = hm.get(task, 0)
            hm[task] += 1
        for task, count in hm.items():
            max_heap.heappush((count, task))
        
        while max_heap.size > 0:
            idx = 0
            temp = []
            while idx < circle_length and max_heap.size > 0:
                if idx < unique_tasks_len:
                    count, task = max_heap.heappop()
                    if count <= 1:
                        intervals += 1
                        idx += 1
                        continue
                    temp.append((count - 1, task))
                intervals += 1
                idx += 1
            for t in temp:
                max_heap.heappush(t)
            if idx < circle_length and max_heap.size > 0:
                intervals += circle_length - idx

        return intervals