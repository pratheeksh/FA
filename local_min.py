def recursive_min(A,i,j):
	mid=i+j/2
	if (A[mid]<=A[mid+1] and A[mid]<= A[mid-1]):
		return A[mid];
	if(A[mid]<=A[mid+1] and A[mid]>=A[mid-1]):
		return recursive_min(A,i,mid)
	else:
		return recursive_min(A,mid,j)

B=[6,7,8,9,10,11,12,13]

x = recursive_min(B,0,7)
print x
print B
