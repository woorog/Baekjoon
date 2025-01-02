from collections import deque
import copy

k = int(input())

for m in range(k):
  a, b = map(int, input().split())
  nl = list(map(int, input().split()))
  sibal = set()
  ans = 155715571557

  q = deque()
  for i in range(a):
    k = copy.deepcopy(nl)
    k.pop(i)
    q.append((nl[i], k))

  while q:

    now, lists = q.pop()
    if now in sibal:
      continue
    if now >= b:
      ans = min(ans, now)
      continue
    for i in range(len(lists)):
      k = copy.deepcopy(lists)
      k.pop(i)
      q.append((now + lists[i], k))
      sibal.add(now)

  aaa = ''.join(['#', str(m + 1)])
  print(aaa, ans - b)
