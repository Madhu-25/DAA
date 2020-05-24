def print_array(a,low,high):
	return a[low:high]
def read_array():
	ip=input("enter list of numbers:")
	l=list(map(int,ip.split()))
	return l
def minimum(a,low,high):
	l=print_array(a,low,high)
	min=0
	for i in range(1,len(l)):
		if(l[min]>l[i]):
			min=i
	return (min + low)
def selectionsort(l):
	for i in range(len(l)-1):
		l[minimum(l,i,len(l))],l[i]=l[i],l[minimum(l,i,len(l))]
	return l
for i in range(3):
	l=read_array()
	print("the sorted array is:",selectionsort(l))

