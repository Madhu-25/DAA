n=int(input("Enter the power: "))
num=n
s=""
while(n>0):
	b=n%2
	s=s+str(b)
	n=n//2
print(s)
M=[[1,1],[1,0]]
term=M
if(s[0]=='1'):
	result=M
else:
	result=[[1,0],[0,1]]

def mult(a,b):
	r=[[0,0],[0,0]]
	for i in range(len(a)):
		for j in range(len(b[0])):
			for k in range(len(b)):
				r[i][j]+=a[i][k]*b[k][j]
	return r
for h in s[1:len(s)]:
	term=mult(term,term)
	if(h=='1'):
		result=mult(result,term)
for i in result:
	print(i)
print(num,"th fibonacci number is: ",result[0][1])
