def  max_subarray(A,low,high,x,y):

    if high==low:
        return(low,high,A[low])
    else:
        mid=(low+high)/2
        left_low,left_high,left_sum=max_subarray(A,low,mid,x,y)
        right_low,right_high,right_sum=max_subarray(A,mid+1,high,x,y)
        cross_low,cross_high,cross_sum,p,q=cross_subarray(A,low,mid,high,x,y)
        if left_sum>right_sum and left_sum>cross_sum:
            return left_low,left_high,left_sum
        if right_sum>left_sum and right_sum>cross_sum:
            return right_low,right_high,right_sum
        return cross_low,cross_high,cross_sum
def cross_subarray(A,low,mid,high,x,y):
    abs_high=x
    abs_low=y
    new_left_sum=new_right_sum=-10000
    sum_i=0
    i=mid
    val= 7
    temp1=-22
    temp2=-22
    k=1
  #  print low,mid,high
    global max_left
    global max_right
    while( i >= low):
        sum_i=sum_i+A[i]
        if (sum_i>new_left_sum):
            new_left_sum=sum_i
            max_left=i
        i=i-1
 #   print "sum_left:", sum_i
    sum_left=sum_i
    sum_i=0

    i=mid+1
    while(i<=high):
        sum_i=sum_i+A[i]
        if (sum_i>new_right_sum):
            new_right_sum=sum_i
            max_right=i
        i=i+1
#    print "sum_right:",sum_i
    sum_right=sum_i
    if(high<=k):
        temp1= val-sum_right
    elif(low>k):
        temp2=val+sum_left
    elif(low<=k and high>k):
        temp1=val+sum_right
        temp2=val-sum_left
    if(temp1<abs_low):
        if(temp2<temp1):
            abs_low=temp2
        else:
            abs_low=temp1
    if(temp1>abs_high):
        if(temp2>temp1):
            abs_high=temp2
        else:
            abs_high=temp1

    print abs_high,abs_low
    return (max_left,max_right,new_left_sum+new_right_sum,abs_high,abs_low)
B=[5,14,1,2,7,8,3,4,11]

C=[]
for i in range(0,8):
    C.append(B[i+1]-B[i])
D=[10,11,7,10,6]
A=[1,-4,3,-4]
print D
print A
global abs_high

global abs_low
abs_high = 7
abs_low = 7
i,j,sum_max=max_subarray(A,0,3,abs_high,abs_low)
print i,j,sum_max
