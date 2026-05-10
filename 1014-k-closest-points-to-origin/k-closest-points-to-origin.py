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
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        self.max_heap = MaxHeap()
        def distance(point):
            return (point[0] * point[0]) + (point[1] * point[1])
        for i, point in enumerate(points):
            dis = distance(point)
            self.add((dis, point), k)
        for point in self.max_heap.heap_arr[1:k+1]:
            ans.append(point[1])
        return ans

            
    def add(self, dis, k):
        self.max_heap.heappush(dis)
        if self.max_heap.size > k:
            self.max_heap.heappop()