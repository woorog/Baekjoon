from collections import defaultdict

dicts = defaultdict(int)

num = int(input())

for i in range(num):
    temp = input()

    if '.' in temp:
        extension = temp[temp.rfind('.') + 1:]  
        dicts[extension] += 1 


for ext, count in sorted(dicts.items()):
    print(f"{ext} {count}")
