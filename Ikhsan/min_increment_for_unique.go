package leetcode_project

import "sort"

func minIncrementForUnique(nums []int) int {
	sort.Ints(nums)

	numTracker := 0
	minIncrement := 0

	for _, num := range nums {
		if numTracker < num {
			numTracker = num
		}
		minIncrement += numTracker - num
		numTracker++
	}

	return minIncrement
}
