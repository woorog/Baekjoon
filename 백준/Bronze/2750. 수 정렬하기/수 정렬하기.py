n = int(input())  # 첫 줄에 수의 개수 N을 입력받음
a = [int(input()) for _ in range(n)]  # N개의 수를 입력받아 리스트에 저장

a.sort()  # 리스트를 오름차순으로 정렬

for num in a:
    print(num)  # 정렬된 리스트를 순서대로 출력
