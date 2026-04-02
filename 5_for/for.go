package main 
import "fmt"

//for ->it is only loop in go

func main(){
	// implement while loop using for
	// i:= 1
	// for i<=3{
	// fmt.Println(i)
	// i=i+1
	// }

	//infinite loop
// 	for{
// 		fmt.Println("1")
// 	}
    
    //classic for loop
    // for i:= 0; i<=3; i++{
	// 	if i==2{
	// 		continue
	// 	}
	// 	// break
	// 	fmt.Println(i)
	// }

	// for i:= range 3{
	// 	fmt.Println(i)
	// }

	for i:=range 10{
		fmt.Println(i)
	}

}