# This application shows how page rank algorythm can be used to create a rating of artists based on how they influenced
# other groups

from page_rank import PageRank

pr = PageRank()

# Starting from Coldplay

pr.addAll1('Coldplay', ['Radiohead', 'U2', 'Oasis', 'The Verve', 'Travis'])
pr.addAll1('Radiohead', ['The Beatles', 'Pink Floyd', 'R.E.M.', 'Neil Young', 'The Smiths'])
pr.addAll1('U2', ['The Clash', 'David Bowie', 'Joy Division', 'Patti Smith', 'The Ramones'])
pr.addAll1('Oasis', ['The Beatles', 'The Rolling Stones', 'The Who', 'The Kinks', 'Sex Pistols'])
pr.addAll1('The Verve', ['The Beatles', 'Pink Floyd', 'The Rolling Stones', 'The Stone Roses', 'The Smiths'])
pr.addAll1('Travis', ['Radiohead', 'Oasis', 'The Beatles', 'R.E.M.', 'The Stone Roses'])
pr.addAll1('The Beatles', ['Chuck Berry', 'Buddy Holly', 'Elvis Presley', 'Little Richard', 'Carl Perkins'])
pr.addAll1('Pink Floyd', ['The Beatles', 'Syd Barrett', 'The Moody Blues', 'King Crimson', 'Frank Zappa'])
pr.addAll1('R.E.M.', ['The Byrds', 'Patti Smith', 'Velvet Underground', 'The Clash', 'Television'])
pr.addAll1('Neil Young', ['Bob Dylan', 'Hank Williams', 'Elvis Presley', 'The Everly Brothers', 'The Beatles'])
pr.addAll1('The Smiths', ['David Bowie', 'Roxy Music', 'The Velvet Underground', 'Patti Smith', 'Iggy Pop'])
pr.addAll1('The Clash', ['The Ramones', 'The Sex Pistols', 'Bob Dylan', 'The Rolling Stones', 'David Bowie'])
pr.addAll1('David Bowie', ['Little Richard', 'Elvis Presley', 'Lou Reed', 'John Lennon', 'Syd Barrett'])
pr.addAll1('Joy Division', ['David Bowie', 'The Velvet Underground', 'Iggy Pop', 'Kraftwerk', 'Roxy Music'])
pr.addAll1('The Ramones', ['The Stooges', 'The Velvet Underground', 'The Beach Boys', 'Chuck Berry', 'The Beatles'])
pr.addAll1('Chuck Berry', ['Nat King Cole', 'Louis Jordan', 'Muddy Waters', 'T-Bone Walker', 'Frank Sinatra'])
pr.addAll1('Buddy Holly', ['Elvis Presley', 'Chuck Berry', 'Little Richard', 'Hank Williams', 'Bill Monroe'])
pr.addAll1('Elvis Presley', ['Arthur Crudup', 'B.B. King', 'Roy Acuff', 'Dean Martin', 'Hank Snow'])
pr.addAll1('Little Richard', ['Sister Rosetta Tharpe', 'Mahalia Jackson', 'Billy Wright', 'Roy Brown', 'B.B. King'])
pr.addAll1('Carl Perkins', ['Elvis Presley', 'Muddy Waters', 'Blind Lemon Jefferson', 'Bill Monroe', 'Jimmie Rodgers'])
pr.addAll1('Syd Barrett', ['The Beatles', 'Pink Floyd', 'The Shadows', 'Bob Dylan', 'Bo Diddley'])


rating = pr.createRating()

print("Rating is: " + str(rating))

