def rotate(arr, m, n, k ,p , cmd):
    temp=[]
    if(cmd=='R'):
        temp=arr[p-1][k:]
        temp.extend(arr[p-1][:k])
        arr[p-1]=temp
    elif(cmd=='C'):
        for i in range(m):
            temp.append(arr[i][p-1])
        j=0
        temp2=temp[k:]+temp[:k]
        print(temp2)
        for i in range(m):
          arr[i][p-1]=temp2[j]
          j+=1

    
    return arr
    
k=int(input('k: '))
p=int(input('p: '))
cmd=input('cmd: ')
print('matrix: ')
mat=[]

while(1):
    row = list(map(int, input().split()))
    if(len(row)==0):
        break
    mat.append(row)
arr = rotate(mat,len(mat),len(mat[0]),k,p,cmd)
for i in range(len(arr)):
  for j in range(len(arr[0])):
    print(arr[i][j], end=" ")
  print('\n')

        
