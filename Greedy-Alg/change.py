'''
denominations= 1,5,10
sample input:
21

sample output:
3
'''

n=int(input())
count=0 
if(n>=10):
    count+=n//10
    n=n%10
if(n>=5):
    count+=n//5
    n=n%5
count+=n
print(count)
    
