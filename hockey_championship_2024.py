from page_rank import PageRank

pr = PageRank()

pr.add("Switzerland", "Norway", 2)
pr.add("Norway", "Switzerland", 5)

pr.add("Czechia", "Finland", 0)
pr.add("Finland", "Czechia", 1)

pr.add("Great Britain", "Canada", 4)
pr.add("Canada", "Great Britain", 2)

pr.add("Austria", "Denmark", 5)
pr.add("Denmark", "Austria", 1)

pr.add("Norway", "Czechia", 6)
pr.add("Czechia", "Norway", 3)

pr.add("Finland", "Great Britain", 0)
pr.add("Great Britain", "Finland", 8)

pr.add("Denmark", "Canada", 5)
pr.add("Canada", "Denmark", 1)

pr.add("Austria", "Switzerland", 6)
pr.add("Switzerland", "Austria", 5)

pr.add("Norway", "Finland", 4)
pr.add("Finland", "Norway", 1)

pr.add("Switzerland", "Czechia", 1)
pr.add("Czechia", "Switzerland", 2)

pr.add("Denmark", "Norway", 2)
pr.add("Norway", "Denmark", 0)

pr.add("Canada", "Austria", 6)
pr.add("Austria", "Canada", 7)

pr.add("Czechia", "Denmark", 4)
pr.add("Denmark", "Czechia", 7)

pr.add("Switzerland", "Great Britain", 0)
pr.add("Great Britain", "Switzerland", 3)

pr.add("Finland", "Austria", 3)
pr.add("Austria", "Finland", 2)

pr.add("Canada", "Norway", 1)
pr.add("Norway", "Canada", 4)

pr.add("Great Britain", "Denmark", 4)
pr.add("Denmark", "Great Britain", 3)

pr.add("Czechia", "Austria", 0)
pr.add("Austria", "Czechia", 4)

pr.add("Denmark", "Switzerland", 8)
pr.add("Switzerland", "Denmark", 0)

pr.add("Canada", "Finland", 3)
pr.add("Finland", "Canada", 5)

pr.add("Czechia", "Great Britain", 1)
pr.add("Great Britain", "Czechia", 4)

pr.add("Norway", "Austria", 4)
pr.add("Austria", "Norway", 1)

pr.add("Switzerland", "Canada", 3)
pr.add("Canada", "Switzerland", 2)

pr.add("Great Britain", "Norway", 5)
pr.add("Norway", "Great Britain", 2)

pr.add("Finland", "Denmark", 1)
pr.add("Denmark", "Finland", 3)

pr.add("Austria", "Great Britain", 4)
pr.add("Great Britain", "Austria", 2)

pr.add("Canada", "Czechia", 3)
pr.add("Czechia", "Canada", 4)

pr.add("Finland", "Switzerland", 3)
pr.add("Switzerland", "Finland", 1)

rating = pr.createRating()
print("Rating is: " + str(rating))


