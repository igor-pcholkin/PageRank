# This application shows how page rank algorythm can be used to create a rating of artists based on how they influenced
# other groups

from page_rank import createRating, toMap1

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

# rowLikeCapacity should be set to the value such that sum of all "likes" influencing specific subject 
# (i.e. group in this # case) should be equal 1.
# In all the declarations above all influencing groups receive an equal influencing score 1 which is then divided by
# rowLikeCapacity (inside createRating()) to receive an absolute influencing score 0.2 (1/rowLikeCapacity = 0.2).
# Sum of all "likes" of each group is equal to 1 because 0.2 * 5 = 1 ( where 5 is a total number of influencing groups)
rowLikeCapacity = 5

totalLikes = { "The Beatles": theBeatlesLikes, "Pink Floyd": pinkFloysLikes, "The Smiths": smithsLikes,
"Talking Heads": talkingHeadsLikes, "Miles Davis": milesDavisLikes, "Aphex Twin": aphexTwinsLikes,
"Kraftwerk": kraftwerkLikes, "Can": canLikes, "R.E.M.": remLikes, "David Bowie": davidBowieLikes }

for key in totalLikes:
	totalLikes[key] = toMap1(totalLikes[key])

rating = createRating(totalLikes, rowLikeCapacity)

print("Rating is: " + str(rating))

# The most influencial groups go first in the rating
assert rating == ['The Velvet Underground', 'The Beatles', 'Elvis Presley', 'Little Richard', 'Karlheinz Stockhausen', 'Roxy Music', 'David Bowie', 'Brian Eno', 'Buddy Holly', 'Chuck Berry', 'The Everly Brothers', 'The Kinks', 'The Beach Boys', 'Neu!', 'Big Star', 'Cabaret Voltaire', 'Kraftwerk', 'Thelonious Monk', 'Syd Barrett', 'Patti Smith', 'T. Rex', 'Tangerine Dream', 'Charlie Parker', 'Television', 'The Byrds', 'The Mothers of Invention', 'John Coltrane', 'Frank Zappa', 'The New York Dolls', 'Duke Ellington', 'Dizzy Gillespie', 'The Rolling Stones', 'Cream', 'Parliament-Funkadelic', 'Aphex Twin', 'Miles Davis', 'Can', 'Pink Floyd', 'R.E.M.', 'Talking Heads', 'The Smiths']
