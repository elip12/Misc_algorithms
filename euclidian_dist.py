# simple python algorithm to compute distance between 2 n-dimensional points
# p1 and p2 can be lists
def euclidian_dist1(p1, p2):
	if len(p1) != len(p2):
		print('p1 has', len(p1), 'dimensions and p2 has', len(p2), 
		      'dimensions; please input points with the same number of dimensions')
		return -1
	dist = 0
	for i in range(len(p1)):
		dist += (p1[i] - p2[i])**2
	return sqrt(dist)
