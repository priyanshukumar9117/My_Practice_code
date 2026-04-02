package main 

import "fmt"

const age = 30

func main(){
	const name="golang"
	// name="javascript"
	fmt.Println(name)

	fmt.Println(age)
	fmt.Println("the age of constant is: ",age)

	const(
		port = 5000
		host = "localhost"
	)

	fmt.Println(port,host)
}