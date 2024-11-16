import heapq

def min(card_bundles):
    heapq.heapify(card_bundles)
    total_comparisons = 0

    while len(card_bundles) > 1:
        
        first = heapq.heappop(card_bundles)
        second = heapq.heappop(card_bundles)
        current_comparison = first + second
        total_comparisons += current_comparison

       
        heapq.heappush(card_bundles, current_comparison)

    return total_comparisons


card_bundles = []
num=int(input())

for i in range(num):
    card_bundles.append(int(input()))
print(min(card_bundles))  
