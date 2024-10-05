# a test with non equal likes

from page_rank import createRating

aLikes = { "B": 4, "C": 4 }
bLikes = { "C": 3 }
cLikes = { "A": 10 }

totalLikes = { "A": aLikes, "B": bLikes, "C": cLikes }

rating = createRating(totalLikes)
print("Rating is: " + str(rating))
assert rating == ["C", "A", "B"]
