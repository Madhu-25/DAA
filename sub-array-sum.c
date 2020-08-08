#include <stdio.h>
int main()
{
    int arr[10],l;
    scanf("%d",&l);
    for(int i=0;i<l;i++){
        scanf("%d",&arr[i]);
    }
    int k;
    scanf("%d",&k);
    int count=0;
    for(int i=0;i<l;i++){
        if(arr[i]<k){
            count++;
        }
    }
    for(int i=0;i<l;i++)
    {
        int m=arr[i];
        for(int j=i+1;j<l;j++)
        {
            m=m+arr[j];
            if(m<k){
                count++;
            }
            else{
                break;
            }
        }
    }
    printf("%d",count);
    
}

/*
input:

5                                                                                                                     
1 11 2 3 15                                                                                                           
10

output:
4

*/
