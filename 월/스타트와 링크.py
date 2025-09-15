from itertools import combinations as c

n = int(input())
r = range(n)
graph = [list(map(int, input().split())) for _ in r]
ans = []

for case in map(set, (temp for temp in c(r,n//2) if 0 in temp)):
   score = 0

   for x,y in c(r, 2):
      value = graph[x][y] + graph[y][x]
      if x in case and y in case:
         score += value
      if x not in case and y not in case:
         score -= value

   ans += [abs(score)]

print(min(ans))
