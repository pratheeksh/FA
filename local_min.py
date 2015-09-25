def local_minimum(A,i,n):
	if(A[0]<=A[1]):
		return A[0]
	if(A[n-1]>=A[n]):
		return A[n]
	return recursive_min(A,1,n-1)
def recursive_min(A,i,j):
	mid=i+j/2
	if (A[mid]<=A[mid+1] and A[mid]<= A[mid-1]):
		return A[mid];
	if(A[mid]<=A[mid+1] and A[mid]>=A[mid-1]):
		return recursive_min(A,i,mid)
	else:
		return recursive_min(A,mid,j)

B=[10,8,8,8,8,8,8,8]
x = local_minimum(B,0,7)
print x
print B
