package leetcode_project

import "math/big"

func addStrings(num1 string, num2 string) string {
	bigNum1 := new(big.Int)
	bigNum2 := new(big.Int)

	bigNum1, ok := bigNum1.SetString(num1, 10)
	if !ok {
		return ""
	}
	bigNum2, ok = bigNum2.SetString(num2, 10)
	if !ok {
		return ""
	}

	result := new(big.Int).Add(bigNum1, bigNum2)

	return result.String()
}
