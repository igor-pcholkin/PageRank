# PageRank

This project enables creation of a ranking system for subjects based on their "likes" using the `PageRank` algorithm. The PageRank algorithm is traditionally used to rank web pages, where the most authoritative pages appear first. A web page is considered more authoritative or credible if it has many links pointing to it, especially from other credible pages.

The same concept can be applied to various "subjects"—such as users, products, music artists, companies, etc.—which can be ranked based on how many "likes" they receive from other subjects, i.e., members of the same network.

`page_rank.py` contains the core algorithm (the `createRating()` function).

`music_rating_test_10.py` provides an example application that calculates the ranking of music artists based on how often they have influenced other artists.
