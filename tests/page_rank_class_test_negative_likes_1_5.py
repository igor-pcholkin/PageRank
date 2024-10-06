from page_rank import PageRank

pr = PageRank(1, 5)
# now 1 and 5 are not relative but absolute values,
# when adding 1 like from one person to another 1 is treated as a "bad" score by itself
# Persons who explicitly don't receive any likes receive a default average value 3. 

pr.add("Person1", "Person2", 5)
pr.add("Person2", "Person2", 5)
pr.add("Person3", "Person2", 5)
pr.add("Person4", "Person3", 5)
pr.add("Person3", "Person1", 5)

rating = pr.createRating()

print("Rating is: " + str(rating))
assert rating == ['Person2', 'Person3', 'Person1', 'Person4']

# negative likes
# NegativePerson1 and NegativePerson2 try to udermine rating of Person2
# the both are unauthoritative persons
pr.add("NegativePerson1", "Person2", 1)
pr.add("NegativePerson2", "Person2", 1)

rating = pr.createRating()

print("Rating is: " + str(rating))
assert rating == ['Person2', 'Person3', 'Person1', 'Person4', 'NegativePerson2', 'NegativePerson1']


