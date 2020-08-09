
#include <stdio.h>
#include<string.h>
#include<ctype.h>
int main()
{
    char string[50];
    char camel_case[50];
    scanf("%[^\n]%*c",string);
    int flag=0,c=0;
    for(int i=0;i<strlen(string);i++)
    {
        if(isspace(string[i]))
        {
            flag=1;
            continue;
        }
        if(flag==1)
        {
            camel_case[c++]=toupper(string[i]);
        }
        else{
            camel_case[c++]=string[i];
        }
        flag=0;
    }
    printf("%s",camel_case);
}


/*
input: 
Thats what she said!

output:
ThatsWhatSheSaid!
*/
