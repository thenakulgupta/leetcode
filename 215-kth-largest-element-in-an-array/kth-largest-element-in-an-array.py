class MinHeap:
    def __init__(self):
        self.heap_arr = [-1]
        self.size = 0
        pass

    def heapify(self, arr):
        self.heap_arr = [-1] + arr
        self.size = len(arr)
        n = self.size
        for i in range(n // 2, 0, -1):
            curr = i
            while True:
                smallest = curr
                left = 2*curr
                right = 2*curr + 1

                if left <= n and self.heap_arr[smallest] > self.heap_arr[left]:
                    smallest = left
                if right <= n and self.heap_arr[smallest] > self.heap_arr[right]:
                    smallest = right

                if curr == smallest:
                    break

                if smallest != curr:
                    self.heap_arr[smallest], self.heap_arr[curr] = self.heap_arr[curr], self.heap_arr[smallest]

                curr = smallest

    def heappush(self, val):
        self.size += 1
        self.heap_arr.append(val)
        current_idx = self.size
        parent_idx = current_idx // 2
        while parent_idx > 0 and self.heap_arr[parent_idx] > self.heap_arr[current_idx]:
            self.heap_arr[current_idx], self.heap_arr[parent_idx] = self.heap_arr[parent_idx], self.heap_arr[current_idx]
            current_idx = parent_idx
            parent_idx = current_idx // 2

    def heappop(self):
        n = self.size
        self.heap_arr[1], self.heap_arr[n] = self.heap_arr[n], self.heap_arr[1]

        pop_value = self.heap_arr.pop()
        self.size -= 1
        n -= 1

        parent_idx = 1
        while True:
            largest = parent_idx
            left = parent_idx * 2
            right = parent_idx * 2 + 1

            if left <= n and self.heap_arr[largest] > self.heap_arr[left]:
                largest = left

            if right <= n and self.heap_arr[largest] > self.heap_arr[right]:
                largest = right

            if largest == parent_idx:
                break

            self.heap_arr[largest], self.heap_arr[parent_idx] = self.heap_arr[parent_idx], self.heap_arr[largest]

            parent_idx = largest

        return pop_value

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.min_heap = MinHeap()
        for num in nums:
            self.add(num, k)
        return self.min_heap.heap_arr[1]


    def add(self, num, k):
        if self.min_heap.size < k or self.min_heap.heap_arr[1] < num:
            self.min_heap.heappush(num)
            if self.min_heap.size > k:
                self.min_heap.heappop()