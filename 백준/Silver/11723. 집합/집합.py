import sys
input = sys.stdin.readline

n = int(input())
s = bin(0)
for i in range(n):
    op = input().split()
    if(op[0]=="check"):
        if int(s,2) & (2**int(op[1])):
            print(1)
        else:
            print(0)
    elif(op[0]=="remove"):
        s = bin(int(s,2) & ~(2**int(op[1])))
    elif(op[0]=="add"):
        s = bin(int(s,2) | (2**int(op[1])))
    elif(op[0]=="toggle"):
        s = bin(int(s,2) ^ (2**int(op[1])))
    elif(op[0]=="all"):
        s = bin(2**21-1)
    elif(op[0]=="empty"):
        s = bin(0)
