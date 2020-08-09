#include <stdio.h>
#include<string.h>
int c=0;
void binary(int n, int arr[], int i)
{
    if(n==i)
    {
        int one=0;
        int zero=0;
        for(int j=0;j<n;j++)
        {
            if(arr[j]==0){
                zero++;
            }
            else{
                one++;
            }
            
        }
        if(one%2==0 && zero%2==0 && one>0 && zero>0) // condition - only strings with even no of 0s and even no of 1s are allowed
        {
            c++;
            for(int j=0;j<n;j++)
            {
                printf("%d",arr[j]);
            }
            printf("\n");
            
        }
        
        return;
    }
    
    arr[i]=0;
    binary(n,arr,i+1);
    
    arr[i]=1;
    binary(n,arr,i+1);
    
}
int main()
{
    int l,arr[20];
    scanf("%d",&l);
    binary(l,arr,0);
    printf("\n Total number of accepted states: %d",c);
    return 0;
}

/* 
input:
4

output:
0011                                                                                                                    
0101                                                                                                                    
0110                                                                                                                    
1001                                                                                                                    
1010                                                                                                                    
1100                                                                                                                    
                                                                                                                        
 Total number of accepted states: 6    
 */
