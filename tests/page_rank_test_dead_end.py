# test checking how a "dead-end" node with all "to" nodes set to 0 is avoided

from page_rank import createRating

aLikes = { "B": 4, "D": 4 }
bLikes = { "C": 8 }
cLikes = { "A": 8 }

totalLikes = { "A": aLikes, "B": bLikes, "C": cLikes }

rating = createRating(totalLikes)
print("Rating is: " + str(rating))
assert rating == ["A", "C", "B", "D"]
