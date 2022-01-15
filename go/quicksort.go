package main

import "fmt"

func Partition(nums []int, start int, end int) int {
	pivot := nums[start]
	i, j := start, start+1
	for ; j < end; j++ {
		if nums[j] <= pivot {
			i++
			nums[i], nums[j] = nums[j], nums[i]
		}
	}
	nums[start], nums[i] = nums[i], nums[start]
	return i
}

func QuickSort(nums []int, start int, end int) []int {
	if start < end-1 {
		partition := Partition(nums, start, end)
		QuickSort(nums, start, partition)
		QuickSort(nums, partition+1, end)
	}
	return nums
}

func sortArray(nums []int) []int {
	// Quick sort
	return QuickSort(nums, 0, len(nums))
}

func main() {
	nums := []int{7, 5, 6}
	fmt.Println(sortArray(nums))
}
