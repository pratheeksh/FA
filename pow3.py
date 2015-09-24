def  bla(n):
    if (n==1):
        return 1
    return (bla(n/3)+bla(n/3))
def cla(n):
    if n==1:
        return 1
    return 2*cla(n/3)
a =bla(27)
b =bla(9)
print a
c = bla(81)
print b
print c
d = cla(81)
print d
