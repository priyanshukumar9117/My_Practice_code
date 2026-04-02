package main

import "fmt"

func main() {

	//int -> 0, string-> "", bool-> false

	//jb pahle se size pata ho tab hi arrays ka use karte hai otherwise 
	//slice use karate hai wo dynamic hota hai.

	//arrays se fixed size that is predictable and memory optimization
	//and constant time access

	// var arr [4]int  //initially all values are zeros

	// fmt.Println(arr)
	// fmt.Println(len(arr)) //array length

	// arr[0] = 1
	// fmt.Println(arr[0])

	// var vals [4]bool  //initially all values are false
	// vals[2] = true
	// fmt.Println(vals)

	// var name [3]string
	// name[0] = "golang"
	// fmt.Println(name)

	// nums:= [3]int{1,2,3}
	// fmt.Println(nums)

	//2d arrays
	nums := [2][2]int{{4, 5}, {7, 8}}
	fmt.Println(nums)

}
