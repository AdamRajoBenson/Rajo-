w=input()
y=0
for i in w:
  if((i=='0')or(i=='1')):
    y=y+1
if(y==len(w)):
  print("yes")
else:
  print("no")
