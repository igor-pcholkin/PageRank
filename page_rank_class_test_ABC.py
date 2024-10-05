# a very basic "happy-path" test

from page_rank import PageRank

pr = PageRank()
pr.add("A", "B", 4)
pr.add("A", "C", 4)
pr.add("B", "C", 8)
pr.add("C", "A", 8)

rating = pr.createRating()
print("Rating is: " + str(rating))
assert rating == ["C", "A", "B"]
