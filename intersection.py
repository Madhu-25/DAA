import math

class Circle:
  def __init__(self, center, radius):
    self.center=center
    self.radius=radius


def find_area(A,B):
  d=math.hypot(B.center[0]-A.center[0] , B.center[1]-A.center[1])
  if(d>A.radius+B.radius):
    return -1
  a=A.radius*A.radius
  b=B.radius*B.radius
  x=(a-b+d*d)/(2*d)
  z=x*x
  y=math.sqrt(a-z)
  if(d<=abs(B.radius-A.radius)):
    return 3.14*min(a,b)
  return a * math.asin(y / A.radius) + b * math.asin(y / B.radius) - y * (x + math.sqrt(z + b - a))

  
A=Circle([2,3],5)
B=Circle([5,4],6)
print(find_area(A,B))
