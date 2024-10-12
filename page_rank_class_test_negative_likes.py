# using default raiting calculation model for network of people where
# likes have both positive and negative connotation
# it shows that this model is not really suitable for that

from page_rank import PageRank

pr = PageRank()

pr.add("Person1", "Person2", 5)
pr.add("Person2", "Person2", 5)
pr.add("Person3", "Person2", 5)
pr.add("Person4", "Person3", 5)
pr.add("Person3", "Person1", 5)
pr.add("Person5", "Person3", 5)

rating = pr.createRating()

print("Rating is: " + str(rating))
assert rating == ['Person2', 'Person3', 'Person1', 'Person5', 'Person4']

# "negative" likes
pr.add("Person4", "Person2", 1)
pr.add("Person5", "Person2", 1)

# this test shows that a default model of rating calculation doesn't work correctly
# if it is supposed to add "negative" likes (<3) as they still contribute to a positive rating of person
# check console output (eigen vector values) for more info

rating = pr.createRating()

print("Rating is: " + str(rating))
assert rating == ['Person2', 'Person3', 'Person1', 'Person5', 'Person4']

# negative likes
# NegativePerson1 and NegativePerson2 try to udermine rating of Person2
# the both are unauthoritative persons
pr.add("NegativePerson1", "Person2", 1)
pr.add("NegativePerson1", "Person1", 5)
pr.add("NegativePerson2", "NegativePerson1", 5)
pr.add("NegativePerson2", "Person2", 1)

rating = pr.createRating()

# it shows that rating of the person 2 is still much higher than of others
print("Rating is: " + str(rating))
assert rating == ['Person2', 'Person1', 'Person3', 'NegativePerson1', 'Person5', 'Person4', 'NegativePerson2']

