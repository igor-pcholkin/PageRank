import numpy as np
import numpy.linalg as linalg

def createRating(totalLikes):
	subjects = getSubjects(totalLikes)
	subjectToIndexMap = getSubjectToIndexMap(subjects)
	transitionMatrix = getTransitionMatrix(subjects, subjectToIndexMap, totalLikes)
	ev1 = eigenVectorForEigenValue1(transitionMatrix)
	finalRating = getFinalRating(subjects, ev1)
	
	return finalRating

def getSubjects(totalLikes):
	subjectsMap = {}
	
	for subject in totalLikes.keys():
		subjectsMap[subject] = 0

	for likes in totalLikes.values():
		for key in likes.keys():
			subjectsMap[key] = 0	
			
	subjects = list(subjectsMap)
	subjects.sort()	

	print(f"Subjects: {str(subjects)}\n")		
	return subjects
	
def getSubjectToIndexMap(subjects):
	subjectToIndexMap = {}

	# create indexes of each subject
	for i in range(len(subjects)):
		subjectToIndexMap[subjects[i]] = i
			
	return subjectToIndexMap
	
def getTransitionMatrix(subjects, subjectToIndexMap, totalLikes):	
	maxRowLikeCapacity = getMaxRowLikeCapacity(totalLikes)

	transitionMatrix = np.zeros((len(subjects), len(subjects)))

	for fromSubject in totalLikes.keys():
		fromSubjectIdx = subjectToIndexMap[fromSubject] 
		fromSubjectLikes = totalLikes[fromSubject]
		for toSubject in fromSubjectLikes.keys():
			toSubjectIndex = subjectToIndexMap[toSubject]
			toSubjectValue = fromSubjectLikes[toSubject]
			transitionMatrix[toSubjectIndex, fromSubjectIdx] = toSubjectValue / maxRowLikeCapacity

	eliminateDeadEndNodes(transitionMatrix, len(subjects))

	print(f"Transition matrix:\n{transitionMatrix}\n")
	return transitionMatrix

# rowLikeCapacity is a sum of all "likes" from a specific subject
# it should be the same value for all subjects
def getMaxRowLikeCapacity(totalLikes):
	maxRowLikeCapacity = 0

	for fromSubject in totalLikes.keys():
		fromSubjectLikes = totalLikes[fromSubject]
		rowLikeCapacity = sum(fromSubjectLikes.values())
		if maxRowLikeCapacity == 0:
			maxRowLikeCapacity = rowLikeCapacity
		else:
			if rowLikeCapacity != maxRowLikeCapacity:
				print(f"Warning: row like capacity ({rowLikeCapacity}) < max row like capacity ({maxRowLikeCapacity}) for subject: {fromSubject}")
				return -1				
				
	print(f"max row capacity is: {maxRowLikeCapacity}")
	return maxRowLikeCapacity

def eliminateDeadEndNodes(transitionMatrix, matWidthHeight):
	v = 1 / matWidthHeight
	for i in range(matWidthHeight):
		column = transitionMatrix[:,i]
		all_zeros = not np.any(column)
		if all_zeros:
			for j in range(matWidthHeight):
				column[j] = v

def eigenVectorForEigenValue1(transitionMatrix):
	D, V = linalg.eig(transitionMatrix)
	V = V.T

	ev1 = V[near(D, 1.0)][0]
	print(f"Eigen vector for eigen value 1: {ev1}\n")
	
	absev1 = abs(ev1)
	print(f"Abs eigen vector for eigen value 1: {absev1}\n")	
	
	return absev1

# needed to find value which is "close enough" to target value
# to find eigen vector corresponding to eigen value 1
def near(a, b, rtol = 1e-5, atol = 1e-8):
    return np.abs(a-b)<(atol+rtol*np.abs(b))

def getFinalRating(subjects, ev1):
	sorted_indices = ev1.argsort()[::-1]
	print(f"Sorted indices of subjects (desc): {sorted_indices}\n")
	
	final_rating = np.array(subjects)[[sorted_indices]]
	return final_rating[0].tolist()	

# assign value likes to all subjects in array
def toMap(arr, value):
	map = {}
	for a in arr:
		map[a] = value
	return map		

# assign 1 like to all subjects in array	
def toMap1(arr):
	return toMap(arr, 1)			
	
