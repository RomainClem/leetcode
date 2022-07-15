def median(lst):
    lstLen = len(lst)
    index = (lstLen - 1) // 2
   
    if (lstLen % 2):
        return lst[index]
    else:
        return (lst[index] + lst[index + 1])/2.0
    
def merge_sorted_list(l1,l2):
    l1_i = 0
    for i in range(len(l2)):
        if l2[i] > l1[-1]:
            l1.append(l2[i])
            continue
        while True:
            if l2[i] <= l1[l1_i]: 
                l1.insert(l1_i, l2[i])
                break
            l1_i += 1
    return l1

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_arr = merge_sorted_list(nums1, nums2) if len(nums1) > len(nums2) else merge_sorted_list(nums2, nums1)
        return(median(merged_arr))