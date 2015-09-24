#!/bin/python
def eval2(p, x, s, e):
    if ( e-s == 1 ):
        return p[s]+x*p[e]
    k = p[(s+e)/2]*pow(x,(e-s)/2)
    lhs = eval2(p, x, s, (s+e)/2)
    rhs = eval2(p, x, (s+e)/2, e)

    return (lhs+ pow(x,(e-s)/2)*rhs - k)
#-(p[e/2]*pow(x,n/2))
def eval3(p, x, s, e, a):
    if (e-s == 1):
        return p[s]+x*p[e]
    num = a[(e-s)/2]
    k= p[(s+e)/2]*num

    lhs = eval3(p, x, s, (s+e)/2, a)
    rhs = eval3(p, x, (s+e)/2, e, a)
    return (lhs+ num*rhs - k)
p = [2,4,1,3,1]
x = 2
print p
ans = eval2(p,x,0,4)
i =1
po =1
a = []
for i in range(3):
    a.append(po)
    po=po*x
print a
ans2 = eval3(p,x,0,4,a)

print ans
print ans2
