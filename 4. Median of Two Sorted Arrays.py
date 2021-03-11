class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        low, high, k, nums1_mid, nums2_mid = 0, len(nums1), (len(nums1) + len(nums2) + 1)>>1, 0 , 0
        while low <= high:
            ## nums1 : ... nums1[nums1_mid - 1] | nums1[nums1_mid] ...
            ## nums2 : ... nums2[nums2_mid - 1] | nums2[nums2_mid] ...
            nums1_mid = low + ((high-low)>>1)
            nums2_mid = k - nums1_mid
            if nums1_mid > 0 and nums1[nums1_mid - 1] > nums2[nums2_mid]:
                high = nums1_mid - 1
            elif nums1_mid != len(nums1) and nums1[nums1_mid] < nums2[nums2_mid - 1]:
                low = nums1_mid + 1
            else:
                break
        if nums1_mid == 0:
            mid_left = nums2[nums2_mid - 1]
        elif nums2_mid == 0:
            mid_left = nums1[nums1_mid - 1]
        else:
            mid_left = max(nums1[nums1_mid - 1], nums2[nums2_mid - 1])
        if (len(nums1) + len(nums2))%2 == 1:
            return mid_left
        if nums1_mid == len(nums1):
            mid_right = nums2[nums2_mid]
        elif nums2_mid == len(nums2):
            mid_right = nums1[nums1_mid]
        else:
            mid_right = min(nums1[nums1_mid], nums2[nums2_mid])
        return (mid_left + mid_right)/2
