#include<stdio.h>
struct pair{
    int min;
    int max;
};

struct pair getMinMax(int arr[],int low,int high){
    struct pair minmax,mml,mmr;
    int mid;
    if(low==high){
        minmax.min=arr[low];
        minmax.max=arr[low];
        return minmax;
    }
    if(low==high-1){
        if(arr[low]>arr[high]){
            minmax.min=arr[high];
            minmax.max=arr[low];
        }
        else{
            minmax.min=arr[low];
            minmax.max=arr[high];
        }
        return minmax;
    }
    mid=(low+high)/2;
    mml=getMinMax(arr,low,mid);
    mmr=getMinMax(arr,mid+1,high);
    if(mml.min<mmr.min){
        minmax.min=mml.min;
    }
    else{
        minmax.min=mmr.min;
    }
    if(mml.max>mmr.max){
        minmax.max=mml.max;
    }
    else{
        minmax.max=mmr.max;
    }
    return minmax;
}

int main(){
    int arr[]={5,7,2,3,8};
    int n=sizeof(arr)/sizeof(arr[0]);
    struct pair minmax=getMinMax(arr,0,n-1);
    printf("minimum is: %d",minmax.min);
    printf("maximum is: %d",minmax.max);
    return 0;
}
