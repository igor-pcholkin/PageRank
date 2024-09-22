# This application shows how page rank algorythm can be used to create a rating of artists based on their influences

from page_rank import createRating, toMap1

theBeatlesLikes = toMap1([ "The Everly Brothers", "Chuck Berry", "Buddy Holly", "Little Richard", "Elvis Presley"])
pinkFloysLikes = toMap1([ "The Rolling Stones", "The Beatles", "Cream", "The Velvet Underground", "Syd Barrett" ])
smithsLikes = toMap1([ "The Velvet Underground", "The New York Dolls", "Roxy Music", "T. Rex", "David Bowie" ])
talkingHeadsLikes = toMap1([ "The Velvet Underground", "Roxy Music", "David Bowie", "Brian Eno", "Parliament-Funkadelic" ])
milesDavisLikes = toMap1([ "Duke Ellington", "Charlie Parker", "Dizzy Gillespie", "John Coltrane", "Thelonious Monk" ])
aphexTwinsLikes = toMap1([ "Brian Eno", "Kraftwerk", "Karlheinz Stockhausen", "Tangerine Dream", "Cabaret Voltaire" ])
kraftwerkLikes = toMap1([ "The Beach Boys", "The Velvet Underground", "The Beatles", "Karlheinz Stockhausen", "Neu!" ])
canLikes = toMap1([ "The Velvet Underground", "Frank Zappa", "The Mothers of Invention", "Karlheinz Stockhausen", "The Beatles" ])
remLikes = toMap1([ "The Byrds", "The Velvet Underground", "Patti Smith", "Big Star", "Television" ])
davidBowieLikes = toMap1([ "The Velvet Underground", "The Beatles", "Little Richard", "Elvis Presley", "The Kinks" ])

rowLikeCapacity = 5

totalLikes = { "The Beatles": theBeatlesLikes, "Pink Floyd": pinkFloysLikes, "The Smiths": smithsLikes,
"Talking Heads": talkingHeadsLikes, "Miles Davis": milesDavisLikes, "Aphex Twin": aphexTwinsLikes,
"Kraftwerk": kraftwerkLikes, "Can": canLikes, "R.E.M.": remLikes, "David Bowie": davidBowieLikes }

rating = createRating(totalLikes, rowLikeCapacity)

print("Rating is: " + str(rating))

assert rating == ['The Velvet Underground', 'The Beatles', 'Elvis Presley', 'Little Richard', 'Karlheinz Stockhausen', 'Roxy Music', 'David Bowie', 'Brian Eno', 'Buddy Holly', 'Chuck Berry', 'The Everly Brothers', 'The Kinks', 'The Beach Boys', 'Neu!', 'Big Star', 'Cabaret Voltaire', 'Kraftwerk', 'Thelonious Monk', 'Syd Barrett', 'Patti Smith', 'T. Rex', 'Tangerine Dream', 'Charlie Parker', 'Television', 'The Byrds', 'The Mothers of Invention', 'John Coltrane', 'Frank Zappa', 'The New York Dolls', 'Duke Ellington', 'Dizzy Gillespie', 'The Rolling Stones', 'Cream', 'Parliament-Funkadelic', 'Aphex Twin', 'Miles Davis', 'Can', 'Pink Floyd', 'R.E.M.', 'Talking Heads', 'The Smiths']