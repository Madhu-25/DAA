def lcs(str1, str2):
  m=len(str1)
  n=len(str2)
  l = [[0 for i in range(n+1)] for j in range(m+1)]
  for i in range(m+1):
    for j in range(n+1):
      if(i==0 or j==0 ):
        l[i][j]=0
      elif(str1[i-1]==str2[j-1]):
        l[i][j]=l[i-1][j-1]+1
      else:
        l[i][j]=max(l[i][j-1],l[i-1][j])
  ind=l[m][n]
  temp=[]
  i=m
  j=n
  while(i>0 and j>0):
    if(str1[i-1]==str2[j-1]):
      temp.insert(ind-1,str1[i-1])
      i-=1
      j-=1
      ind-=1
    elif(l[i-1][j]>l[i][j-1]):
      i-=1
    else:
      j-=1
  return temp

l=lcs("this is her text","the text")
n=len("this is her text")-len(l)
print(n*4)

