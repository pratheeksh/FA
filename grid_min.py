def grid_min(A,i1,j1,i2,j2):
	midx=i1+i2/2
	midy=j1+j2/2
	print midx,midy
	if(A[midx][midy]<=A[midx+1][midy] and A[midx][midy]<=A[midx-1][midy]):
		if(A[midx][midy]<=A[midx][midy+1] and A[midx][midy]<=A[midx][midy-1]):
			return (A[midx][midy])
		
		elif(A[midx][midy]<=A[midx][midy+1] and A[midx][midy]>=A[midx][midy-1]):
			return grid_min(A,i1,j1,i2,midy)
		
		elif(A[midx,midy]>=A[midx][midy+1] and A[midx,midy]<=A[midx][midy-1]):
			return grid_min(A,i1,midy,i2,j2)
		elif(A[midx][midy+1]>A[midx][midy-1]):
			return grid_min(A,i1,j1,i2,midy)
		else:
			return grid_min(A,i1,midy,i2,j2)
	elif(A[midx][midy]<=A[midx+1][midy] and A[midx][midy]>=A[midx-1][midy]):
		return grid_min(A,i1,j1,midx,j2)
	elif(A[midx][midy]>=A[midx+1][midy] and A[midx,midy]<=A[midx-1][midy]):
		return grid_min(A,midx,j1,i2,j2)
	elif(A[midx+1][midy]<=A[midx-1][midy]):
		return grid_min(A,midx,j1,i2,j2)
	else:
		return grid_min(A,i1,j1,midx,j2)


Matrix = [[0 for x in range(5)] for x in range(5)] 
for i in range(5):
	for j in range(5):
		Matrix[j][i]=(i+1)*(j+1)
		print Matrix[j][i],
	print " "
Matrix[0][0]=100
x = grid_min(Matrix,0,0,4,4)
print x
