# test to try to use also negative values for rating

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
#assert rating == ['Person2', 'Person3', 'Person1', 'Person5', 'Person4']

# try to undermine rating of the person 2 
pr.add("Person4", "Person2", -5)
pr.add("Person5", "Person2", -5)

rating = pr.createRating()

print("Rating is: " + str(rating))
#assert rating == ['Person2', 'Person3', 'Person1', 'Person5', 'Person4']

pr.add("NegativePerson1", "Person2", -5)
pr.add("NegativePerson1", "Person1", 5)
pr.add("NegativePerson2", "NegativePerson1", 5)
pr.add("NegativePerson2", "Person2", -5)

rating = pr.createRating()

print("Rating is: " + str(rating))
#assert rating == ['Person2', 'Person1', 'Person3', 'NegativePerson1', 'NegativePerson2', 'Person5', 'Person4']

