#include<stdio.h>

void printArray(int arr[],int n){
    for(int i=0;i<n;i++){
        printf("%d\t",arr[i]);
    }
    printf("\n");
}
void swap(int arr[],int i,int j){
    int temp;
    temp=arr[i];
    arr[i]=arr[j];
    arr[j]=temp;
}
int partition(int arr[],int low,int high){
    int pivot=arr[high];
    int i=low-1;
     //int n=high+low-1;
     for(int j=low;j<high;j++){
        if(arr[j]<pivot){
            i++;
            swap(arr,i,j);
        }
     }
     swap(arr,i+1,high);
     return i+1;
    }


void quickSort(int arr[],int low,int high){
    int pi;
    if(low<high){
        pi=partition(arr,low,high);
        quickSort(arr,low,pi-1);
        quickSort(arr,pi+1,high);
    }
}

int main(){
    int arr[]={0,0,0,-1,-2};
    int n=sizeof(arr)/sizeof(arr[0]);
    printf("size of array is: %d",n);
    printf("given array is: ");
    printArray(arr,n);
    int low=0;
    int high=n-1;
    quickSort(arr,low,high);
    printf("sorted array is: ");
    printArray(arr,n);
    return 0;
}