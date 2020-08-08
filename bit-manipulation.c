#include <stdio.h>
#include<string.h>

int main()
{
    char str[20];
    scanf("%[^\n]%*c", str); 
    int shift[20];
    int n;
    n=strlen(str);
    for(int i=0;i<n;i++){
        if(str[i]!=' '){
            shift[i]=n-i-1;
        }
        else{
            shift[i]=0;
        }
    }
    char new_str[20];
    for(int i=0;i<n;i++)
    {
        int c;
        c=str[i];
        if((c+shift[i])>122)
        {
            int l;
            l=(c+shift[i])-122;
            new_str[i]=96+l;
            printf("%c",new_str[i]);
            
        }
        else{
            new_str[i]=str[i]+shift[i];
            printf("%c",new_str[i]);
        }
    }
    return 0;
}
