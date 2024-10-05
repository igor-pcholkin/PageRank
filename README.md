# PageRank

This project enables creation of a ranking system for subjects based on their "likes" using the `PageRank` algorithm. The PageRank algorithm is traditionally used to rank web pages, where the most authoritative pages appear first. A web page is considered more authoritative or credible if it has many links pointing to it, especially from other credible pages.

The same concept can be applied to various "subjects"—such as users, products, music artists, companies, etc.—which can be ranked based on how many "likes" they receive from other subjects, i.e., members of the same network.

`page_rank.py` contains the core algorithm (the `createRating()` function).

## API
There are two ways (two APIs) to obtain a rating:

1. Using a single function call, e.g.
```
createRating({ "A": aLikes, "B": bLikes, "C": cLikes })
```
3. Using OOP Api, where "likes" can be added gradually:
```pr = PageRank()
pr.add("A", "B", 4)
pr.add("A", "C", 4)
pr.add("B", "C", 8)
pr.add("C", "A", 8)

rating = pr.createRating()
```

## Notes
Beware of the message "Warning: row like capacity < max row like capacity" - more likely the rating will be calculated incorrectly with it.
Also ensure that eigen values are randomly distributed within 0..1 interval, they should not be too low.

## Examples
`music_rating_*.py` - example applications that calculate the ranking of music artists based on how often they have influenced other artists.
