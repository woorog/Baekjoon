def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    point=-1

    for ny,nx in targets:
        
        if ny >= point:
            answer += 1
            point = nx
    
    
    return answer