#include <stdio.h>
#include<string.h>

int max(int a, int b)
{
    if(a>b){
        return a;
    }
    return b;
}
void lcs(char x[], char y[])
{
    int m=strlen(x);
    int n=strlen(y);
    int L[20][20];
    for(int i=0;i<=m;i++)
    {
        for(int j=0;j<=n;j++)
        {
            if(i==0 || j==0){
                L[i][j]=0;
            }
            else if(x[i-1]==y[j-1])
            {
                L[i][j]=L[i-1][j-1]+1;
            }
            else
            {
                L[i][j]=max(L[i-1][j],L[i][j-1]);
            }
        }
    }
    int ind=L[m][n];
    char str[20];
    int i=m;
    int j=n;
    while(i>0 && j>0){
        if(x[i-1]==y[j-1])
        {
            str[ind-1]=x[i-1];
            i--;
            j--;
            ind--;
        }
        else if(L[i-1][j]>L[i][j-1])
        {
            i--;
        }
        else{
            j--;
        }
    }
    printf("The longest common subsequence: %s",str);
}

int main()
{
    char x[20],y[20];
    scanf("%s",x);
    scanf("%s",y);
    lcs(x,y);
    return 0;
}

/*
input:
aggtab                                                                                                                  
gxtxayab

output:
The longest common subsequence: gtab 

*/
