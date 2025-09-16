Y,X,y,x,k=map(int,input().split())
a=[list(map(int,input().split()))for _ in range(Y)]
k=[0,0,0,0,0,0]
d=[1,-1,0,0]
for i in list(map(int,input().split())):
 if 0<=y+d[4-i]<Y and 0<=x+d[i-1]<X:
  y+=d[4-i];x+=d[i-1]
  if i==1:k=[k[3],k[1],k[0],k[5],k[4],k[2]]
  elif i==2:k=[k[2],k[1],k[5],k[0],k[4],k[3]]
  elif i==3:k=[k[4],k[0],k[2],k[3],k[5],k[1]]
  elif i==4:k=[k[1],k[5],k[2],k[3],k[0],k[4]]
  if a[y][x]==0:a[y][x]=k[5]
  else:k[5]=a[y][x];a[y][x]=0
  print(k[0])
