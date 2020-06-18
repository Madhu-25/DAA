#this algorithm gives the minimum number of points to cover the line segments
''' Sample input:
4                                                                                                                                              
4 7                                                                                                                                            
1 3                                                                                                                                            
2 5                                                                                                                                            
5 6 


Sample output:
2                                                                                                                                              
3 6 

''' 

n=int(input())
points=[]
for i in range(n):
    ip=input().split(' ')
    points.append([int(ip[0]),int(ip[1])])
    
End_points=sorted(points, key=lambda points:points[1])
Beg_points=sorted(points, key=lambda points:points[0])


T=Beg_points[0][0]-1
L=[]
for i in range(n-1):
    x,y=End_points[i]
    if(x>T):
        L.append(y)
        T=y
        
if(L[len(L)-1]<End_points[len(End_points)-1][0]):
    if(End_points):
        L.append(End_points[len(End_points)-1][0])
        
print(len(L))
print(*L)
