def merge(m,p,middle,q):


    c=[]
    i=p
    j=middle+1
    k=0
    count=0
    while( i<= middle and j <= q):
        if(m[j]<m[i]):
            count = count+(middle+1-i)
            c.append(m[j])
            j = j + 1
        else:
            c.append(m[i])
            i = i + 1
        k = k + 1
    while(k<=q-p):
        if(i<=middle):
            c.append(m[i])
            i =i + 1
        else:
            c.append(m[j])
            j = j + 1

        k = k+1
    k=p
    t=0
    while(k<=q):
        m[k]=c[t]
        k= k+1
        t= t+1

    print m
    return count
def sort_count(m,i,j):
    if i>=j:
        return 0
    print m,i,j
    mid =(j+i)/2
    c1=sort_count(m,i,mid)
    c2=sort_count(m,mid+1,j)
    c3=merge(m,i,mid,j)
    return (c1+c2+c3)
a=[5,6,11,13,17]
b=[2,3,8,9,19]
a=[1,10]
b=[4,5]
n=[1,3,5,6,10,2,7]
k = sort_count(n,0,6)
print k
