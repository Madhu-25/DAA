'''
List A contains the profit per click on each ad
List B contains the average number of clicks on each partition
the function maxProfit returns the maximum profit we can get by arranging the ads in the partions


sample input:
3                                                                                                                                              
1 3 -5                                                                                                                                         
-2 4 1 

Sample output:
23
'''


def maxProfit(A,B):
    S=0
    while(A and B):
        a=max(A)
        b=max(B)
        A.remove(a)
        B.remove(b)
        S+=(a*b)
    return S


n=int(input())
A=[int(i) for i in input().split()]
B=[int(i) for i in input().split()]
print(maxProfit(A,B))
