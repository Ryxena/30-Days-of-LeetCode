package leetcode_project

func reverse(x int) int {
	x32 := int32(x)

	result := int32(0)
	base := int32(10)
	for x32 != 0 {
		d := x32 % base
		x32 /= base

		newResult := result*base + d
		if (newResult-d)/base != result {
			return 0
		}

		result = newResult
	}

	return int(result)
}
