# This application shows how page rank algorythm can be used to create a rating of artists based on how they influenced
# other groups

from page_rank import PageRank

# each line here shows artist and groups which influenced it
theBeatlesLikes = [ "The Everly Brothers", "Chuck Berry", "Buddy Holly", "Little Richard", "Elvis Presley"]
pinkFloysLikes = [ "The Rolling Stones", "The Beatles", "Cream", "The Velvet Underground", "Syd Barrett" ]
smithsLikes = [ "The Velvet Underground", "The New York Dolls", "Roxy Music", "T. Rex", "David Bowie" ]
talkingHeadsLikes = [ "The Velvet Underground", "Roxy Music", "David Bowie", "Brian Eno", "Parliament-Funkadelic" ]
milesDavisLikes = [ "Duke Ellington", "Charlie Parker", "Dizzy Gillespie", "John Coltrane", "Thelonious Monk" ]
aphexTwinsLikes = [ "Brian Eno", "Kraftwerk", "Karlheinz Stockhausen", "Tangerine Dream", "Cabaret Voltaire" ]
kraftwerkLikes = [ "The Beach Boys", "The Velvet Underground", "The Beatles", "Karlheinz Stockhausen", "Neu!" ]
canLikes = [ "The Velvet Underground", "Frank Zappa", "The Mothers of Invention", "Karlheinz Stockhausen", "The Beatles" ]
remLikes = [ "The Byrds", "The Velvet Underground", "Patti Smith", "Big Star", "Television" ]
davidBowieLikes = [ "The Velvet Underground", "The Beatles", "Little Richard", "Elvis Presley", "The Kinks" ]

pr = PageRank()

pr.addAll1('The Beatles', theBeatlesLikes)
pr.addAll1('Pink Floyd', pinkFloysLikes)
pr.addAll1('The Smiths', smithsLikes)
pr.addAll1('Talking Heads', talkingHeadsLikes)
pr.addAll1('Miles Davis', milesDavisLikes)
pr.addAll1('Aphex Twin', aphexTwinsLikes)
pr.addAll1('Kraftwerk', kraftwerkLikes)
pr.addAll1('Can', canLikes)
pr.addAll1('R.E.M.', remLikes)
pr.addAll1('David Bowie', davidBowieLikes)

rating = pr.createRating()

print("Rating is: " + str(rating))

# The most influencial groups go first in the rating
assert rating == ['The Velvet Underground', 'The Beatles', 'Karlheinz Stockhausen', 'Little Richard', 'Elvis Presley', 'Brian Eno', 'Roxy Music', 'David Bowie', 'Buddy Holly', 'Chuck Berry', 'The Everly Brothers', 'The Kinks', 'Neu!', 'The Beach Boys', 'Big Star', 'Tangerine Dream', 'Kraftwerk', 'Cabaret Voltaire', 'Thelonious Monk', 'Duke Ellington', 'Dizzy Gillespie', 'Frank Zappa', 'Cream', 'Charlie Parker', 'John Coltrane', 'Parliament-Funkadelic', 'Patti Smith', 'Syd Barrett', 'T. Rex', 'Television', 'The Byrds', 'The Mothers of Invention', 'The New York Dolls', 'The Rolling Stones', 'Aphex Twin', 'Miles Davis', 'Pink Floyd', 'R.E.M.', 'Talking Heads', 'Can', 'The Smiths']
