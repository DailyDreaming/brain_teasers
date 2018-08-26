# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = nums1 + nums2
        half = len(l) // 2
        l.sort()
        if not len(l) % 2:
            return (l[half - 1] + l[half]) / 2.0
        return l[half]
