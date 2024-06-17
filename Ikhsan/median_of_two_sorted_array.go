package leetcode_project

import "sort"

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	sortArray := append(nums1, nums2...)
	sort.Ints(sortArray)
	n := len(sortArray)

	if n%2 == 0 {
		return float64(sortArray[n/2-1]+sortArray[n/2]) / 2.0
	} else {
		return float64(sortArray[n/2])
	}
}
