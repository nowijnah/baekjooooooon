n = int(input())

p = []
p = [0 for i in range(n*2)]
cnt=[]
cnt=[1 for _ in range(n)]

for i in range(n):
    p[i*2], p[i*2+1] = map(int, input().split())

for i in range(n):
    for j in range(n):
        if(p[i*2]<p[j*2] and p[i*2+1]<p[j*2+1]):
            cnt[i]+=1

print(*cnt)