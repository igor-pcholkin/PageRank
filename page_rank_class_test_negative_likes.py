from page_rank import PageRank

pr = PageRank()

pr.add("Person1", "Person2", 5)
pr.add("Person2", "Person2", 5)
pr.add("Person3", "Person2", 5)
pr.add("Person4", "Person3", 5)
pr.add("Person3", "Person1", 5)

print("Rating is: " + str(pr.createRating()))

# negative likes
# NegativePerson1 and NegativePerson2 try to udermine rating of Person2
# the both are unauthoritative persons
pr.add("NegativePerson1", "Person2", 1)
pr.add("NegativePerson1", "Person1", 5)
pr.add("NegativePerson2", "NegativePerson1", 5)
pr.add("NegativePerson2", "Person2", 1)

# it shows that rating of the person 2 is still much higher than of others
print("Rating is: " + str(pr.createRating()))


