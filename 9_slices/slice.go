package main
import "fmt"

//slice -> dynamic
//most used construct in go
// + useful methods

func main(){
    
	//uninitialized slice is nil
	// var nums []int
	// fmt.Println(nums)
	// fmt.Println(nums == nil) //true
	// fmt.Println(len(nums))

	// var nums= make([]int, 2, 5)  //initially all values are zeros
    
	//capacity -> maximum number of element can fit
	// fmt.Println(cap(nums))
	// fmt.Println(nums)
	// fmt.Println(nums==nil)

	// nums = append(nums, 1)
	// nums = append(nums, 2)
	// nums = append(nums, 3)
	// nums = append(nums, 4)
	// fmt.Println(nums)
	// fmt.Println(cap(nums))

	// var nums = make([]int, 0, 5)
	// nums= append(nums, 1, 2, 3, 4)
	// nums= append (nums, 41, 47, 87)
	// fmt.Println(nums)
	// fmt.Println(cap(nums))
	// fmt.Println(len(nums))


	nums :=[]int{} 
	nums = append(nums, 5)
	nums = append(nums,8, 7, 9, 10)
	nums = append(nums, 9)
	nums = append(nums, 8)
	fmt.Println(nums)
	fmt.Println(cap(nums))
	fmt.Println(len(nums))

}