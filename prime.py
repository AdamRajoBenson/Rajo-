p=int(input())
q=0
r=1 
while r<=p: 
  if p%r==0:
      q=q+1 
  r=r+1
if q==2:
  print('yes')
else: 
  print('no')
