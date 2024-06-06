package leetcode_project

func CommonChars(words []string) []string {
	if len(words) == 0 {
		return []string{}
	}
	charCounts := make(map[rune]int)
	for _, val := range words[0] {
		charCounts[val]++
	}

	for i := 1; i < len(words); i++ {
		tempCounts := make(map[rune]int)
		for _, char := range words[i] {
			if _, exists := charCounts[char]; exists {
				tempCounts[char]++
			}
		}

		for char := range charCounts {
			if tempCounts[char] < charCounts[char] {
				charCounts[char] = tempCounts[char]
			}
		}
	}

	res := []string{}
	for char, count := range charCounts {
		for i := 0; i < count; i++ {
			res = append(res, string(char))
		}
	}
	return res
}
