from itertools import permutations
n = int(input())

num = []
num = [(i+1) for i in range(n)]

per = list(permutations(num,n))

for i in per:
    print(*i)