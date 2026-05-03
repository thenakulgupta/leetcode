class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        m, n = len(nums1), len(nums2)
        _max = (m + n) // 2
        i, j = 0, m
        while i <= j:
            mid = (i + j) // 2
            p2 = (m + n + 1) // 2 - mid

            left1  = float('-inf') if mid == 0 else nums1[mid - 1]
            right1 = float('inf')  if mid == m else nums1[mid]

            left2  = float('-inf') if p2 == 0 else nums2[p2 - 1]
            right2 = float('inf')  if p2 == n else nums2[p2]

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return max(left1, left2)
                return (max(left1, left2) + min(right1, right2)) / 2

            elif left1 > right2:
                j = mid - 1
            else:
                i = mid + 1
        return 0.0