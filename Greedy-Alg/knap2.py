import numpy as np
global n
n, W= map(int, input().split()) 


 
Values=[]
Weights=[]

for i in range(n):
    ip = input().split(' ')
    Values.append(int(ip[0]))
    Weights.append(int(ip[1]))
    
    
    
def knapsack(W,w,v):
    A=[0]*n
    V=0
    for i in range(n):
        if(W==0):
            return V,A 
        a=min(w[i],W)
        V+=a*(v[i]/w[i])
        w[i]=w[i]-a
        A[i]+=a 
        W-=a 
    return V,A 

def msort(v, w):
	if(len(v)>1):
		mid=len(v)//2
		Lv=v[:mid]
		Rv=v[mid:]
		Lw=w[:mid]
		Rw=w[mid:]
		msort(Lv,Lw)
		msort(Rv,Rw)
		i=0
		j=0
		k=0
		while(i<len(Lv) and j<len(Rv)):
			if((Lv[i]/Lw[i])>(Rv[j]/Rw[j])):
				v[k]=Lv[i]
				w[k]=Lw[i]
				i+=1
			else:
				v[k]=Rv[j]
				w[k]=Rw[j]
				j+=1
			k+=1
		while(i<len(Lv)):
			v[k]=Lv[i]
			w[k]=Lw[i]
			i+=1
			k+=1
		while(j<len(Rv)):
		    v[k]=Rv[j]
		    w[k]=Rw[j]
		    j+=1
		    k+=1
		
msort(Values,Weights)

Val, Amt=knapsack(W,Weights,Values)
print(round(float(Val),4))


