"""

there are totally 5 states A,B,C,D,E
all processes are initially in state A
the state transitions 'AB 2' implies that process 2 changes from state A to B
find the processes in each state

input format :
# of processes
# of transitions
transitions

input: 
10
8
AB 2
AB 4
AB 5
AD 6
AD 7
AE 10
DE 6
BD 5
"""

def process(list1, p, n):
  d={'A':[],'B':[],'C':[],'D':[],'E':[]}
  lookup={}  
  
  for each in list1:
    if(each[3]=='1' and each[4]=='0'):
      if 10 not in lookup.keys():
        lookup[10]=each[1]
        d[each[1]].append(10)
        continue
      else:
        temp=lookup[10]
        d[temp].remove(10)
        lookup[10]=each[1]
        d[each[1]].append(10)
        continue


    
    c=int(each[3])
    if c not in lookup.keys():
      lookup[c]=each[1]
      d[each[1]].append(c)
    else:
      temp=lookup[c]
      d[temp].remove(c)
      lookup[c]=each[1]
      d[each[1]].append(c)

  lis=lookup.keys()
  processes=[i for i in range(1,p+1)]
  not_alloted=list(set(processes)-set(lis))
  for i in not_alloted:
    d['A'].append(i)
 
  for each in d.keys():
    print('\n',each,end="")
    tmp=sorted(d[each])
    
    for i in tmp:
      print(' ',i,end="")


   

  
  
  
  
  
    
p=int(input())
n=int(input())
lis=[]
for i in range(n):
  string=input()
  lis.append(string)
process(lis,p,n)
