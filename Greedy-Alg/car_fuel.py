'''this algorithm gives the minimum number of refills needed for a car with mileage 'tank' to travel from 0 to 'dest'
the number of intermideate fuel stops = n

Sample input:
950                                                                                                                                           
400                                                                                                                                           
4                                                                                                                                             
200 375 550 750

Sample output:
2


returns -1 if not possible
'''


def minRefill(x,n,L):
    if(x[len(x)-1]<L):
        return 0
    numRefills=0
    currRefill=0
    while(currRefill<=n):
        lastRefill=currRefill
        while(currRefill<=n and (x[currRefill+1]-x[lastRefill])<=L):
            currRefill+=1 
        if(currRefill==lastRefill):
            return -1
        if(currRefill<=n):
            numRefills+=1 
    return numRefills
    
dest=int(input())
tank=int(input())
n=int(input())
x=[0]
x+=[int(i) for i in input().split()]
x.append(dest)
print(minRefill(x,n,tank))
