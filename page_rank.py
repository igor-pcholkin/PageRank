import numpy as np
import numpy.linalg as linalg

# needed to find value which is "close enough" to target value
# to find eigen vector corresponding to eigen value 1
def near(a, b, rtol = 1e-5, atol = 1e-8):
    return np.abs(a-b)<(atol+rtol*np.abs(b))

aLikes = { "B": 4, "C": 4 }
bLikes = { "C": 8 }
cLikes = { "A": 8 }

rowLikeCapacity = 8
# TODO:need to ensure that sum(values) of each xLikes = rowLikeCapacity

totalLikes = { "A": aLikes, "B": bLikes, "C": cLikes }
subjectsMap = {}

for likes in totalLikes.values():
	for key in likes.keys():
		subjectsMap[key] = 0	
		
subjects = list(subjectsMap)
subjects.sort()	

# create indexes of each subject
for i in range(len(subjects)):
	subjectsMap[subjects[i]] = i	
		
print(subjects)

likesMat = np.zeros((len(subjects), len(subjects)))

for fromSubject in totalLikes.keys():
	fromSubjectIdx = subjectsMap[fromSubject] 
	fromSubjectLikes = totalLikes[fromSubject]
	for toSubject in fromSubjectLikes.keys():
		toSubjectIndex = subjectsMap[toSubject]
		toSubjectValue = fromSubjectLikes[toSubject]
		likesMat[toSubjectIndex, fromSubjectIdx] = toSubjectValue / rowLikeCapacity

print(likesMat)

D, V = linalg.eig(likesMat)
V = V.T

ev1 = V[near(D, 1.0)]
print(ev1)

sorted_indices = ev1.argsort()[::-1]
print(sorted_indices)	
print(np.array(subjects)[sorted_indices])

#ev1 = np.array([2, 1, 2])
#sorted_indices = ev1.argsort()[::-1]
#print(sorted_indices)

#ev1 = np.array([3, 2, -4, 0, 1, -9])
#sorted_indices = ev1.argsort()[::-1]
#print(sorted_indices)

	
