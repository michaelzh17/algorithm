#!/usr/bin/env python3

def merge_a(nums1, m, nums2, n):
    start = 0
    nums1 = nums1[:m]
    nums2_cp = nums2.copy()
    for i in nums2:
        for j in range(start, len(nums1)):
            if i <= nums1[j]:
                nums1.insert(j, i)
                nums2_cp.remove(i)
                start = j
                break
    nums1 += nums2_cp
    return nums1

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

m = 3
n = 3

print(merge_a(nums1, m, nums2, n))
