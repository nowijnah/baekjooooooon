import sys
input = sys.stdin.readline

n = 1000000
p = [1,1]+[0]*999998
primes = []

for i in range(2,int(n**(1/2))+1):
    if(p[i]==0):
        primes.append(i)
        for j in range(2*i,n, i):
            # print(j)
            p[j] = 1

# print(p)
# print(primes)

n = int(input())
while(n!=0):
    i = primes[1]
    j = 0
    while(1):
        if(n-i<i):
            print("Goldbach's conjecture is wrong.")
            break
        if(p[n-i]==0):
            print(n , "=" , i , "+" , n-i)
            break
        j+=1
        i = primes[j]
    n = int(input())