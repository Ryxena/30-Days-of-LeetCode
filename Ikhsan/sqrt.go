package leetcode_project

func MySqrt(x int) int {
	opr := 1
	for {
		if opr*opr > x {
			return opr - 1
		}
		if opr*opr == x {
			return opr
		}
		opr++
	}
}
