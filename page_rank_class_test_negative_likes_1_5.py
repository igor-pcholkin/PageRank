from page_rank import PageRank1to5

pr = PageRank1to5()
# now 1 and 5 are not relative but absolute values,
# when adding 1 like from one person to another 1 is treated as a "bad" score by itself
# Persons who explicitly don't receive any likes receive a default value somewhere between 1 and 5. 

pr.add("Person1", "Person2", 5)
pr.add("Person2", "Person2", 5)
pr.add("Person3", "Person2", 5)
pr.add("Person4", "Person3", 5)
pr.add("Person3", "Person1", 5)
pr.add("Person5", "Person3", 5)

rating = pr.createRating()

print("Rating is: " + str(rating))
assert rating == ['Person2', 'Person3', 'Person1', 'Person5', 'Person4']

# negative likes
pr.add("Person4", "Person2", 1)
pr.add("Person5", "Person2", 1)

rating = pr.createRating()

print("Rating is: " + str(rating))
#assert rating == ['Person2', 'Person3', 'Person1', 'Person5', 'Person4']

# negative likes
pr.add("NegativePerson1", "Person2", 1)
pr.add("NegativePerson2", "Person2", 1)

rating = pr.createRating()

print("Rating is: " + str(rating))
assert rating == ['Person2', 'Person3', 'Person1', 'NegativePerson1', 'NegativePerson2', 'Person5', 'Person4']


