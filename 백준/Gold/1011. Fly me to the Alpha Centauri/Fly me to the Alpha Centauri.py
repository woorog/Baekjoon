t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    d = y - x
    count = 0  
    move = 1  
    move_plus = 0  
    while move_plus < d :
        count += 1
        move_plus += move  
        if count % 2 == 0 : 
            move += 1
    print(count)