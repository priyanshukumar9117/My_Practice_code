/*#include<stdio.h>
int main(){
    int disp[3][4]={{5,6,8,2},{4,5,3,7},{1,10,13,15}};
    printf("%d\n",disp[2][1]);
    return 0;
}*/

/*#include<stdio.h>
int main(){
    char str1[]="Week-7-Assignment";
    char str2[]={'w','e','e','k','-','7','-','A','s','s','i','g','n','m','e','n','t'};
    int n1=sizeof(str1)/sizeof(str1[0]);
    int n2=sizeof(str2)/sizeof(str2[0]);

    printf("n1=%d,n2=%d",n1,n2);
    return 0;
}*/
/*#include<stdio.h>
#include<string.h>
int main(){
   char p[20];
   char s[]="string";
   int length=strlen(s);
   int i;
   for(i=0;i<length;i++)
     p[i]=s[length-i];
   printf("%s",p);
   return 0;  
}*/

/*#include<stdio.h>
#include<string.h>
int main(){
    static char str1[]="dills";
    static char str2[20];
    static char str3[]="daffo";
    int i;
    i=strcmp(strcat(str3,strcpy(str2,str1)),"daffodils");
    printf("%d",i);
    return 0;
}*/

/*#include<stdio.h>
void foo(),f();
int main(){
    f();
    return 0;
}
void foo(){
    printf("2 ");
}
void f(){
    printf("1 ");
    foo();
}*/

/*#include<stdio.h>
int i;
int fun();
int main(){
    while(i){
        fun();
        main();
    }
    printf("Hello\n");
    return 0;
}
int fun(){
    printf("Hi");
}*/

/*#include<stdio.h>
float func(float age[]);
int main(){
    float result,age[]={23.4,55,22.6,3,40.5,18};
    result=func(age);
    printf("%0.2f",result);
    return 0;
}

float func(float age[]){
    int i;
    float result,sum=0.0;
    for(i=0;i<6;++i){
        sum+=age[i];
    }
    result=(sum/6);
    return result;
}*/

//#include<stdio.h>
/*void func(int n,int sum){
    int k=0,j=0;
    if(n==0) return;
    k=n%10;
    j=n/10;
    sum=sum+k;
    func(j,sum);
    printf("%d,",k);
}*/
/*int fun(int x){
    if(x>100){
        return x-10;
    }
    else{
       return fun(fun(x+11));
    }
}
int main(){
    int b=fun(95);
    printf("%d",b);
    return 0;
}*/


#include<stdio.h>
void bubbleSort(int arr[],int n){
   boolean swapped =false;
}
int main(){
    int arr[]={21,98,32,1};
    int n=sizeof(arr)/sizeof(arr[0]);
    printf("size of array is: %d",n);
    printf("given array is: ");
    printArray(arr,n);
    
    bubbleSort(arr,n);
    printf("sorted array is: ");
    printArray(arr,n);
    return 0;
}