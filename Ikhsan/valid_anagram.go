package leetcode_project

func isAnagram(s string, t string) bool {
	a := make(map[string]int)

	if len(s) != len(t) {
		return false
	}

	for _, v := range s {
		a[string(v)] += 1
	}

	for _, v := range t {
		_, contains := a[string(v)]
		if contains {
			a[string(v)] -= 1
		}
	}

	for _, v := range a {
		if v != 0 {
			return false
		}
	}

	return true
}
