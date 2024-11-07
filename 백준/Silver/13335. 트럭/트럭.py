

nums =list(map(int,input().split()))

num=nums[0]
lens=nums[1]
max=nums[2]

trucks=list(map(int,input().split()))

nlist=[]
now=0
count=0
time=0
while 1:
    
    if len(nlist)>0 and nlist[0][1]==time:
        now-=trucks[nlist[0][0]]
      
        nlist.pop(0)
   

    
    
    if count!=len(trucks) and now+trucks[count] <=max:
        now+=trucks[count]
        nlist.append((count,time+lens))
        count+=1

    time+=1
    if count==len(trucks) and len(nlist)==0 :
        break
    

    
    # print(nlist,now,time)
print(time)        