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
