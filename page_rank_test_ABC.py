# a very basic "happy-path" test

from page_rank import createRating

aLikes = { "B": 4, "C": 4 }
bLikes = { "C": 8 }
cLikes = { "A": 8 }

rowLikeCapacity = 8

totalLikes = { "A": aLikes, "B": bLikes, "C": cLikes }

rating = createRating(totalLikes, rowLikeCapacity)
print("Rating is: " + str(rating))
assert rating == ["C", "A", "B"]
