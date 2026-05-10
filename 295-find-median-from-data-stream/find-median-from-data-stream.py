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


class MedianFinder:

    def __init__(self):
        self.left = MaxHeap()
        self.right = MinHeap()


    def addNum(self, num: int) -> None:
        if self.left.size == 0:
            self.left.heappush(num)
            return

        def balanceHeap():
            if abs(self.left.size - self.right.size) <= 1:
                return
            if self.right.size > self.left.size:
                self.left.heappush(self.right.heappop())
            else:
                self.right.heappush(self.left.heappop())

        if num < self.left.heap_arr[1]:
            self.left.heappush(num)
        else:
            self.right.heappush(num)

        balanceHeap()
        

    def findMedian(self) -> float:
        left_val = self.left
        right_val = self.right
        if left_val.size == right_val.size:
            return (left_val.heap_arr[1] + right_val.heap_arr[1]) / 2
        elif left_val.size > right_val.size:
            return left_val.heap_arr[1]
        else:
            return right_val.heap_arr[1]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()