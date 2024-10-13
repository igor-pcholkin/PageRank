# PageRank rating calculated based on whether a command won or lost.
# also it shows that results are basically consistent with official results,
# except that here Norway and Denmark changed places 

from page_rank import PageRank

pr = PageRank()

pr.add1("Norway", "Switzerland")
pr.add1("Finland", "Czechia")
pr.add1("Great Britain", "Canada")
pr.add1("Austria", "Denmark")
pr.add1("Norway", "Czechia")
pr.add1("Great Britain", "Finland")
pr.add1("Denmark", "Canada")
pr.add1("Austria", "Switzerland")
pr.add1("Norway", "Finland")
pr.add1("Czechia", "Switzerland")
pr.add1("Denmark", "Norway")
pr.add1("Austria", "Canada")
pr.add1("Denmark", "Czechia")
pr.add1("Great Britain", "Switzerland")
pr.add1("Finland", "Austria")
pr.add1("Norway", "Canada")
pr.add1("Great Britain", "Denmark")
pr.add1("Austria", "Czechia")
pr.add1("Denmark", "Switzerland")
pr.add1("Finland", "Canada")
pr.add1("Great Britain", "Czechia")
pr.add1("Norway", "Austria")
pr.add1("Switzerland", "Canada")
pr.add1("Great Britain", "Norway")
pr.add1("Denmark", "Finland")
pr.add1("Austria", "Great Britain")
pr.add1("Czechia", "Canada")
pr.add1("Finland", "Switzerland")

rating = pr.createRating()
print("Rating is: " + str(rating))


