from page_rank import PageRank1to5

pr = PageRank1to5()

pr.add("Adam", "Bob", 5)
pr.add("Bob", "Bob", 5)
pr.add("Declan", "Bob", 5)
pr.add("Susan", "Declan", 5)
pr.add("Declan", "Adam", 5)
pr.add("Jerry", "Declan", 5)

rating = pr.createRating()

print("Rating is: " + str(rating))
assert rating == ['Bob', 'Declan', 'Adam', 'Susan', 'Jerry']

# trying to undermine rating of Bob with negative scores
pr.add("Susan", "Bob", 1)
pr.add("Jerry", "Bob", 1)

rating = pr.createRating()

print("Rating is: " + str(rating))
assert rating == ['Bob', 'Declan', 'Adam', 'Susan', 'Jerry']

# more trying to undermine rating of Bob with negative scores
pr.add("Mark", "Bob", 1)
pr.add("Irina", "Bob", 1)

rating = pr.createRating()

# This shows that Bob's rating can't be affected seriosly when negative scores are provided by non-authoritative people
# see more details in console output
print("Rating is: " + str(rating))
assert rating[0:3] == ['Bob', 'Declan', 'Adam'] # other 4 should have equal rating but can show in changing order


