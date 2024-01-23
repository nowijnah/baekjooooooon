n = int(input())
num=[[0 for i in range(j)] for j in range(n)]
m = []
com = []

for i in range(n):
    num[i] = list(map(int, input().split()))
# print(num)

com = num[-1]
for i in range(n-1):
    # print(com)
    cnt=0
    m = []
    for j in num[n-i-2]:
        # print(j , max(com[cnt],com[cnt+1]))
        m.append(j + max(com[cnt],com[cnt+1]))
        cnt+=1
    com = m
print(*com)