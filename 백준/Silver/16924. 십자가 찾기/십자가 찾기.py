# 6 8
# ....*...
# ...**...
# ..*****.
# ...**...
# ....*...
# ........
import copy
n,m = map(int, input().split())
cross = [[]for _ in range(n)]
check = [[]for _ in range(n)]
for i in range(n):
    cross[i] = list(input())

check = copy.deepcopy(cross)
ans=[]
ccnt=0
# print(cross)

for i in range(1,n-1):
    for j in range(1,m-1):
        cnt=0
        # print(i,j)
        if(cross[i][j]=='*'):
            a,b,c,d=i,j,i,j
            while(a-1>=0 and b+1<m and c+1<n and d-1>=0 and
                cross[a-1][j]=='*' and
                cross[i][b+1]=='*' and
                cross[c+1][j]=='*' and
                cross[i][d-1]=='*'):
                # print(a,b)
                cnt+=1
                ccnt+=1
                ans.append("{} {} {}".format(i+1,j+1,cnt))
                check[i][j]='.'
                check[a-1][j]='.'
                check[i][b+1]='.'
                check[c+1][j]='.'
                check[i][d-1]='.'
                a-=1
                b+=1
                c+=1
                d-=1

ck = 0
# print(check)
for i in check:
    if '*' in i:
        print(-1)
        ck+=1
        break
if(ck==0):
    print(ccnt)
    print(*ans, sep='\n')