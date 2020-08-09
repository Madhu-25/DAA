#include<stdio.h>
int main()
{
    int total,capacity,cost,dist;
    printf("Enter the total no of bananas: ");
    scanf("%d",&total);
    printf("\nEnter the capacity of the camel: ");
    scanf("%d",&capacity);
    printf("\nEnter the cost for travelling 1km: ");
    scanf("%d",&cost);
    printf("\nEnter the total distance to be covered: ");
    scanf("%d",&dist);
    int i=1,f=0;
    int present_dist=0;
    while(total>capacity)
    {
        int no_of_trip=2*(total/capacity)-1;
        int s=capacity/(no_of_trip*cost);
        present_dist+=s;
        total-=capacity;
        if(present_dist>dist)
        {
            f=1;
            total+=(present_dist-dist)*no_of_trip;
            break;
        }
        printf("\nStoppage distance %d #bananas left: %d",present_dist,total);
        i++;
    }
    int dist_left=dist-present_dist;
    if(cost*dist_left>total)
    {
        printf("\nCannot be carried!");
        
    }
    else
    {
        if(f==1)
        {
            printf("\n#bananas that can be carried %d",total);
        }
        else{
            printf("\n#bananas that can be carried %d",total-dist_left*cost);
        }
    }
}

/*
input: 

Enter the total no of bananas: 3000                                                                                     
                                                                                                                        
Enter the capacity of the camel: 1000                                                                                   
                                                                                                                        
Enter the cost for travelling 1km: 1                                                                                    
                                                                                                                        
Enter the total distance to be covered: 1000   

output:
                                                                                                                        
Stoppage distance 200 #bananas left: 2000                                                                               
Stoppage distance 533 #bananas left: 1000                                                                               
#bananas that can be carried 533 

*/
