package leetcode_project

func isHappy(n int) bool {
	last, first := n, squares(n)

	for n != 1 && first != last {
		last = squares(last)
		first = squares(squares(first))
	}
	return first == 1
}

func squares(n int) int {
	res := 0
	for n > 0 {
		lastDigit := n % 10
		// 19 -> 19 % 10 = 9
		// 1 -> 1 % 10 = 1
		res += lastDigit * lastDigit
		n /= 10
	}
	return res
}

// func checkForValue(value int, values ...interface{}) bool {
//     for _,v := range values {
//         if v == value {
//             return true
//         }
//     }
//     return false
// }
