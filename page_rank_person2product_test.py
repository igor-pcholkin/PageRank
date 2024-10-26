# create rating of products based on purchases

from page_rank import PersonToProduct

pr = PersonToProduct()
pr.addAll1("Harry", ["Icecream", "Pepsi", "Hamburger"])
pr.addAll1("Mary", ["Icecream", "Cola"])
pr.addAll1("Bob", ["Frees", "Cola"])
pr.addAll1("John", ["Pepsi", "Cheesburger"])
pr.addAll1("Robert", ["Pepsi", "Nuggets"])
pr.addAll1("Sarah", ["Cola", "Cheesburger"])
pr.addAll1("Declan", ["Frees", "Hamburger"])
pr.addAll1("Stewart", ["Frees", "Cola", "Hamburger"])
pr.addAll1("Michael", ["Nuggets"])

rating = pr.createRating()
print("Rating is: " + str(rating))
assert rating == ['Pepsi', 'Cola', 'Hamburger', 'Icecream', 'Cheesburger', 'Frees', 'Nuggets']
