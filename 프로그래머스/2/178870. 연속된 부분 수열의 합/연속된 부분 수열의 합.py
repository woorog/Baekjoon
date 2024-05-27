def solution(sequence, k):
    answer = [0, 0, float('inf')]  
    alen = len(sequence)
    now = 0
    ptr = 0
    temp = 0

    while ptr < alen:
        temp += sequence[ptr]  

        while temp > k and now <= ptr: 
            temp -= sequence[now]
            now += 1

        if temp == k:
            if ptr - now < answer[2]: 
                answer = [now, ptr, ptr - now]
        
        ptr += 1

    return answer[:2] 