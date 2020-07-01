# calculating euclidean distance between vectors
from math import sqrt

# EuclideanDistance = sqrt(sum for i to N (v1[i] – v2[i])^2)
# calculate euclidean distance
def euclidean_distance(a, b):
	return sqrt(sum((e1-e2)**2 for e1, e2 in zip(a,b)))


# ManhattanDistance = sum for i to N sum |v1[i] – v2[i]|
# calculate manhattan distance
def manhattan_distance(a, b):
	return sum(abs(e1-e2) for e1, e2 in zip(a,b))

# define data
row1 = [10, 20, 15, 10, 5]
row2 = [12, 24, 18, 8, 7]
# calculate distance
e_dist = euclidean_distance(row1, row2)
m_dist = manhattan_distance(row1, row2)

print(e_dist)
print(m_dist)