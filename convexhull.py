import random

def generatePoints(n=20, plane_size=50):
	# Generate a list of n tuples in (x,y) format using list comprehension
	# max_coordinates restricts the size of our plane
	xpoints = [random.randrange(1, plane_size) for x in range(1,n)]
	ypoints = [random.randrange(1, plane_size) for x in range(1,n)]

	return xpoints, ypoints


print(generatePoints())

