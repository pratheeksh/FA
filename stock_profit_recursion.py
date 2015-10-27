def  max_subarray(A,low,high):
    if high==low:
        return(low,high,A[low])
    else:
        mid=(low+high)/2
        left_low,left_high,left_sum=max_subarray(A,low,mid)
        right_low,right_high,right_sum=max_subarray(A,mid+1,high)
        cross_low,cross_high,cross_sum=cross_subarray(A,low,mid,high)
        if left_sum>right_sum and left_sum>cross_sum:
            return left_low,left_high,left_sum
        if right_sum>left_sum and right_sum>cross_sum:
            return right_low,right_high,right_sum
        return cross_low,cross_high,cross_sum
def cross_subarray(A,low,mid,high):

    new_left_sum=new_right_sum=-10000
    sum_i=0
    i=mid
    global max_left
    global max_right
    while( i >= low):
        sum_i=sum_i+A[i]
        if (sum_i>new_left_sum):
            new_left_sum=sum_i
            max_left=i
        i=i-1
    print "sum_left:", sum_i
    sum_i=0

    i=mid+1
    while(i<=high):
        sum_i=sum_i+A[i]
        if (sum_i>new_right_sum):
            new_right_sum=sum_i
            max_right=i
        i=i+1
    print "sum_right:",sum_i
    return (max_left,max_right,new_left_sum+new_right_sum)

B=[5,14,1,2,7,8,3,4,11]
C=[]
for i in range(0,8):
    C.append(B[i+1]-B[i])
print C
i,j,sum_max=max_subarray(C,0,7)
print i,j,sum_max

