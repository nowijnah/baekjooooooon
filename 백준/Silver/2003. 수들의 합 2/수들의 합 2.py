n,m = map(int, input().split())

a = list(map(int, input().split()))

sum,cnt = 0,0
i,j=0,0

while(j<n):
    if(i>=n):
        sum = 0
        j+=1
        continue

    sum += a[i]

    if(sum == m):
        sum = 0
        cnt+=1
        j+=1
        i=j
    elif(sum > m):
        sum = 0
        j+=1
        i=j
    else:
        i+=1

print(cnt)