# test using teleport to avoid cases when isolated isles of nodes absorb most credit
# the scenario is described here: https://towardsdatascience.com/large-graph-analysis-with-pagerank-e571e3dec8ed
# without teleports is still can work however most of nodes will receive value 0 in eigenvector so it is not possible to tell
# the difference among these nodes

from page_rank import createRating

aLikes = { "A": 1, "B": 1, "C": 1, "D": 1 }
bLikes = { "D": 1 }
cLikes = { "D": 1, "E": 1 }
dLikes = { "B": 1 }
eLikes = { "A": 1 }  

totalLikes = { "A": aLikes, "B": bLikes, "C": cLikes, "D": dLikes, "E": eLikes }

rating = createRating(totalLikes)
print("Rating is: " + str(rating))
assert rating == ['D', 'B', 'A', 'E', 'C']
