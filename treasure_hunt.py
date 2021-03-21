def possiblerotation(n,houses,start,fstart):
  if(houses[start]==0):
    return 1
  
  if((start+houses[start]+1)<len(houses)):
    print(start,'\n')
    return possiblerotation(n,houses,houses[start]+start,fstart)
  if((start-houses[start]+1)>=0):
    print(start,'\n')
    return possiblerotation(n,houses,start-houses[start],fstart)
  if(start==fstart):
    return -1
  

def check_hunt(n,houses,start):
  if(possiblerotation(n,houses,start,start)==1):
    print('YES')
  else:
    print('NO')


n=5
start=2
houses=[1,2,1,0,5]
check_hunt(n,houses,start)
'''
harry goes on a teasure hunt. there are an array of houses. Each house has a value.
Harry wins if he reaches the house with value zero. 
The start variable gives the position of the house he starts.
He can move upto the value of the house to the right or left if possible.
eg he starts at 3 that is houses[2] value is 1 he can move one position to the left or one position to the right.
Proceeding this way if he ever reaches 0 the output is YES else NO '''
