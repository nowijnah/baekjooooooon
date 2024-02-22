import sys
input = sys.stdin.readline

from collections import deque
dq = deque()

n = int(input())
for i in range(n):
    op = input().split()
    if(op[0]=="push_front"):
        dq.appendleft(op[1])
    elif(op[0]=="push_back"):
        dq.append(op[1])
    elif(op[0]=="size"):
        print(len(dq))
    elif(op[0]=="empty"):
        if(len(dq)==0):
            print(1)
        else:
            print(0)
    elif(len(dq)==0):
        print(-1)
    elif(op[0]=="pop_front"):
        print(dq.popleft())
    elif(op[0]=="pop_back"):
        print(dq.pop())
    elif(op[0]=="front"):
        d = dq.popleft()
        print(d)
        dq.appendleft(d)
    elif(op[0]=="back"):
        d = dq.pop()
        print(d)
        dq.append(d)
    # print(dq)
