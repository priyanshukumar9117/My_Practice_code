/*void swap(int *a,int *b){
    int *temp;
    *temp=*a;
    *a=*b;
    *b=*temp;
}
int partition(int arr[],int low,int high){
    int pivot=arr[low];
    int i=low+1,j=high;
    while(i<j){
        if(arr[i]>pivot && arr[j]<pivot){
            swap(&arr[i],&arr[j]);
            i++;
            j--;
        }
        if(arr[i]<=pivot){
            i++;
        }
        if(arr[j]>=pivot){
            j--;
        }
        swap(&pivot,&arr[j]);
        return j;
    }
}*/


#include<stdio.h>
int main(){
    int a;
    int arr[5]={1,2,3,4,5};
    arr[1]=++arr[1];
    a=arr[1]++;
    arr[1]=arr[a++];
    printf("%d,%d",a,arr[1]); 
    return 0;
}
