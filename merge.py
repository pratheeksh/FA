def merge(m,p,q):

    b=m[((p+q)/2)+1:q+1]
    a=m[p:(p+q)/2+1]
    print a
    print b
    c=[]
    i=0
    j=0
    k=0
    n=q-p+1
    count=0
    while( i< n/2 and j < n/2):
        if(b[j]<a[i]):
            print b[j],a[i]
            count = count+((n/2)-i)
            c.append(b[j])
            j = j + 1
        else:
            c.append(a[i])
            i = i + 1
        k = k + 1
    while(k<n):
        if(i<n/2):
            c.append(a[i])
            i =i + 1
        else:
            c.append(b[j])
            j = j + 1

        k = k+1
    return count
a=[5,6,11,13,17]
b=[2,3,8,9,19]
a=[1,10]
b=[4,5]
c=[1,10,4,5]
x=merge(c,0,3)
print x
n=[1,3,5,6,10,2,7,9,11,13]
k = merge(n,0,9)
print k
