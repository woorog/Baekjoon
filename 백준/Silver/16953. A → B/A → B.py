from collections import deque
a,b=map(int,input().split())
q=deque()
q.append((b,1))
k=set()
ans=15571557

while q:
  x,y=q.popleft()
  if x==a:
    ans=min(ans,y)
    break;

  if x in k:
    continue
    
  if (x-1)%10==0:
    q.append((int((x-1)/10),y+1))
    k.add(x)
  if x%2==0:
    q.append((int((x/2)),y+1))
    k.add(x)

 

if ans==15571557:
  print(-1)
else:
  print(ans)


  
