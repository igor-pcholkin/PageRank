import numpy as np
import numpy.linalg as linalg

class PageRank():

	def __init__(self, min = 0, max = 0):
		if min == 0 and max == 0:
			self.default = 0
		else:	
			self.default = (max - min + 1) / 2

	totalLikes = {}
	
	def add(self, fromS, to, likes):
		likesTo = self.totalLikes.get(fromS)
		if likesTo == None:
			likesTo = {}
			self.totalLikes[fromS] = likesTo
		likesTo[to] = likes
		
	def addAll1(self, fromS, allTo):
		for to in allTo:
			self.add1(fromS, to)	
		
	def add1(self, fromS, to):
		self.add(fromS, to, 1)	

	def createRating(self):
		return createRating(self.totalLikes, self.default)

def createRating(totalLikes, default = 0):
	subjects = getSubjects(totalLikes)
	subjectToIndexMap = getSubjectToIndexMap(subjects)
	transitionMatrix = getTransitionMatrix(subjects, subjectToIndexMap, totalLikes, default)
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
	
def getTransitionMatrix(subjects, subjectToIndexMap, totalLikes, default):	
	transitionMatrix = np.zeros((len(subjects), len(subjects)))

	for fromSubject in totalLikes.keys():
		fromSubjectIdx = subjectToIndexMap[fromSubject] 
		fromSubjectLikes = totalLikes[fromSubject]
		fromCapacity = getFromCapacity(totalLikes, fromSubject, len(subjects), default)
		for toSubject in subjects:
			toSubjectIndex = subjectToIndexMap[toSubject]
			toSubjectValue = fromSubjectLikes.get(toSubject)
			if toSubjectValue == None:
				toSubjectValue = default
			transitionMatrix[toSubjectIndex, fromSubjectIdx] = toSubjectValue / fromCapacity

	eliminateDeadEndNodes(transitionMatrix, len(subjects))

	print(f"Transition matrix without teleports:\n{transitionMatrix}\n")
	transitionMatrix = addTeleports(transitionMatrix, len(subjects))

	print(f"Transition matrix with teleports:\n{transitionMatrix}\n")
	return transitionMatrix

# https://towardsdatascience.com/large-graph-analysis-with-pagerank-e571e3dec8ed
def addTeleports(transitionMatrix, matWidthHeight):
	dumpingFactor = 0.9
	telMatrix =  np.full((matWidthHeight, matWidthHeight), (1 - dumpingFactor) / matWidthHeight)
	return transitionMatrix * dumpingFactor + telMatrix

def getFromCapacity(totalLikes, fromSubject, matWidthHeight, default):
		fromSubjectLikes = totalLikes[fromSubject]
		likesCapacity = sum(fromSubjectLikes.values())
		defaultCapacity = (matWidthHeight - len(fromSubjectLikes.values())) * default
		fromCapacity = likesCapacity + defaultCapacity
		print(f"From capacity of {fromSubject}: {likesCapacity} + {defaultCapacity} = {fromCapacity}")
		return fromCapacity

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
	
