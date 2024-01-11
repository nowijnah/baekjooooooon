import math
import sys
input = sys.stdin.readline()

n = int(input)
num = []
num = [0]*(n+1)

if(n==1):
    print(0)
elif(n==2 or n==3):
    print(1)
else:
    num[0],num[1],num[2]=0,1,1
    j=4
    while(j!=n+1): #solved
        if(int(math.log(j,3))==math.log(j,3)):
            num[j-1]=int(math.log(j,3))
        elif(j%2!=0 and j%3!=0):
            num[j-1]=num[j-2]+1
        elif(j%2!=0  and j%3==0):
            num[j-1]=min(num[j-2]+1,num[j//3-1]+1)
        elif(j%3!=0):
            num[j-1]=min(num[j-2]+1,num[j//2-1]+1)
        else:
            num[j-1]=min(num[j-2]+1,num[j//2-1]+1,num[j//3-1]+1)
        j+=1
    print(num[n-1])