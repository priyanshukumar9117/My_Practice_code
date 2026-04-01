#include<stdio.h>

void printArray(int arr[],int n){
    for(int i=0;i<n;i++){
        printf("%d\t",arr[i]);
    }
    printf("\n");
}
void heapify(int arr[],int n,int i){
    int largest=i;
    int l=2*i+1;
    int r=2*i+2;

    if(l<n && arr[l]>arr[largest]){
        largest=l;
    }
    if(r<n && arr[r]>arr[largest]){
        largest=r;
    }

    if(largest!=i){
        //swap(arr[largest],arr[i]);
        int temp=arr[i];
        arr[i]=arr[largest];
        arr[largest]=temp;
        heapify(arr,n,largest);
    }
}

void heapSort(int arr[],int n){
    for(int i=n/2-1;i>=0;i--){
        heapify(arr,n,i);
    }

    for(int i=n-1;i>0;i--){
        int temp=arr[0];
        arr[0]=arr[i];
        arr[i]=temp;
        heapify(arr,i,0);
    }
}

int main(){
    int arr[]={21,98,32,1,45,94,36,0,0,0,0,-4,-8,-7,64,53,61,23,85,19,81};
    int n=sizeof(arr)/sizeof(arr[0]);
    printf("size of array is: %d",n);
    printf("given array is: ");
    printArray(arr,n);
    
    heapSort(arr,n);
    printf("sorted array is: ");
    printArray(arr,n);
    return 0;
}