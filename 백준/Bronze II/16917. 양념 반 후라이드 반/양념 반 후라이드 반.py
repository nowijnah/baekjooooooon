a,b,c,x,y = map(int, input().split())

if(a+b > c*2):
    if(c*2 < a and c*2 < b):
        price = c*2*max(x,y)
    else:
        price = c*2*min(x,y)
        if(x>y):
            if(c*2 < a):
                price += (x-y)*c*2
            else:
                price += (x-y)*a
        else:
            if(c*2 < b):
                price += (y-x)*c*2
            else:
                price += (y-x)*b
else:
    price = x*a + y*b

print(price)

#4*2*8 = 64  + 4*2*2 = 16 80