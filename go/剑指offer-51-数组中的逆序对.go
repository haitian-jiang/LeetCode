// hard
// 2022-01-14
func reversePairs(nums []int) int {
    pairs := 0
    sortArray(nums, &pairs)
    return pairs
}

func sortArray(nums []int, pairs *int) []int {
    // MergeSort
    if len(nums) <= 1 {
        return nums
    }
    leftHalf := sortArray(nums[:len(nums)/2], pairs)
    rightHalf := sortArray(nums[len(nums)/2:], pairs)
    i, j, k := 0, 0, 0
    result := make([]int, len(nums))
    for i < len(leftHalf) && j < len(rightHalf) {
        if leftHalf[i] <= rightHalf[j] {
            result[k] = leftHalf[i]
            i++
            k++
        } else {
            result[k] = rightHalf[j]
            j++
            k++
            *pairs += len(leftHalf) - i
        }
    }
    if i < len(leftHalf) {
        for k < len(nums) {
            result[k] = leftHalf[i]
            i++
            k++
        }
    } else if j < len(rightHalf) {
        for k < len(nums) {
            result[k] = rightHalf[j]
            j++
            k++
        }
    }
    return result
}