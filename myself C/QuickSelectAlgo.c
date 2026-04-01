#include<stdio.h>

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

int findKthSmallest(int arr[],int low,int high,int k){
    if(k>0 && k<=high-low+1){
        int index=partition(arr,low,high);
        if(index-low==k-1){
            return arr[index];
        }
        if(index-low > k-1){
            return findKthSmallest(arr,low,index-1,k);
        }
        else{
            return findKthSmallest(arr,index+1,high,k-index+low-1);
        }
    }
}

int main(){
    int arr[]={8,7,5,1,2,3,6,12};
    int low=0;
    int high=7;
    int k=4;
    int ans=findKthSmallest(arr,low,high,k);
    printf("final ans is: %d",ans);
    return 0;
}