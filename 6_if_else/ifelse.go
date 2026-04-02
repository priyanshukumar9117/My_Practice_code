package main 
import "fmt"

func main(){
	// age:=16

	// if age>=18{
	// 	fmt.Println("person is an adult")
	// } else{
	// 	fmt.Println("person is not an adult")
	// }
    
	// if age >= 18 {
	// 	fmt.Println("person is an adult")
	// } else if age >= 12{
	// 	fmt.Println("person is teenager")
	// } else {
	// 	fmt.Println("person is a kid")
	// }

	var role = "admin"
	var hasPermission = false

	if role =="admin" && hasPermission{
		fmt.Println("yes")
	} else {
		fmt.Println("no")
	}

	if role =="admin" || hasPermission{
		fmt.Println("yes")
	} else {
		fmt.Println("no")
	}

	if age:= 25; age>=18{
		fmt.Println("person is an adult and age is:",age)
	} else if age >= 12{
		fmt.Println("person ia a teenager and age is:", age)
	} else {
		fmt.Println("person is a kid and age is:",age)
	}

	//go does not have ternary operator till yet, you will have to use normal if-else

}