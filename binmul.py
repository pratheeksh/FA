def shift (A,n,i):
    c=[]
    k = 0
    j = 0
    while j<n+i:
        print j
        if j<i:
            c.append(0)
        else:
            c.append(A[k])
            k = k+1
        j = j+1

    print c


A = [0,1,1,1,0,1]
n = len(A)
print A
print n

shift(A,n,4)

