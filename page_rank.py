import numpy as np
import numpy.linalg as linalg

# needed to find value which is "close enough" to target value
# to find eigen vector corresponding to eigen value 1
def near(a, b, rtol = 1e-5, atol = 1e-8):
    return np.abs(a-b)<(atol+rtol*np.abs(b))

def createRating(totalLikes, rowLikeCapacity):
# TODO:need to ensure that sum(values) of each xLikes = rowLikeCapacity
	subjectsMap = {}

	for subject in totalLikes.keys():
		subjectsMap[subject] = 0

	for likes in totalLikes.values():
		for key in likes.keys():
			subjectsMap[key] = 0	
			
	subjects = list(subjectsMap)
	subjects.sort()	

	# create indexes of each subject
	for i in range(len(subjects)):
		subjectsMap[subjects[i]] = i	
	
	print(f"Subjects: {str(subjects)}\n")		

	likesMat = np.zeros((len(subjects), len(subjects)))

	for fromSubject in totalLikes.keys():
		fromSubjectIdx = subjectsMap[fromSubject] 
		fromSubjectLikes = totalLikes[fromSubject]
		for toSubject in fromSubjectLikes.keys():
			toSubjectIndex = subjectsMap[toSubject]
			toSubjectValue = fromSubjectLikes[toSubject]
			#print(f"Setting likesMat[{toSubjectIndex}, {fromSubjectIdx}] to {toSubjectValue / rowLikeCapacity}")
			likesMat[toSubjectIndex, fromSubjectIdx] = toSubjectValue / rowLikeCapacity

	eliminateDeadEndNodes(likesMat, len(subjects))

	print(f"Transition matrix:\n{likesMat}\n")

	D, V = linalg.eig(likesMat)
	V = V.T

	ev1 = V[near(D, 1.0)][0]
	print(f"Eigen vector for eigen value 1: {ev1}\n")
	ev1 = abs(ev1)
	print(f"Abs eigen vector for eigen value 1: {ev1}\n")

	sorted_indices = ev1.argsort()[::-1]
	print(f"Sorted indices of subjects (desc): {sorted_indices}\n")
	final_rating = np.array(subjects)[[sorted_indices]]
	
	return final_rating[0].tolist()
	#final_rating_as_string = ', '.join(final_rating[0].tolist())	
	#print(f"Final rating: {final_rating_as_string}")

	#ev1 = np.array([2, 1, 2])
	#sorted_indices = ev1.argsort()[::-1]
	#print(sorted_indices)

	#ev1 = np.array([3, 2, -4, 0, 1, -9])
	#sorted_indices = ev1.argsort()[::-1]
	#print(sorted_indices)

def eliminateDeadEndNodes(likesMat, matWidthHeight):
	v = 1 / matWidthHeight
	for i in range(matWidthHeight):
		column = likesMat[:,i]
		all_zeros = not np.any(column)
		if all_zeros:
			for j in range(matWidthHeight):
				column[j] = v

def toMap(arr, value):
	map = {}
	for a in arr:
		map[a] = value
	return map		
	
def toMap1(arr):
	return toMap(arr, 1)			
	
