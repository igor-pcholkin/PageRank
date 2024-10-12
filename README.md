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
2. Using OOP Api, where "likes" can be added gradually:
```
pr = PageRank()
pr.add("A", "B", 4)
pr.add("A", "C", 4)
pr.add("B", "C", 8)
pr.add("C", "A", 8)

rating = pr.createRating()
```
3. A model where scores 1 to 5 are used instead of likes. This model allows to use negative "likes", where 1 and 2 produce negative effect to those to whom the likes are transferred. 3 has a neutral meaning, 4 and 5 have positive one.
```
pr = PageRank1to5()
pr.add("A", "B", 5) # add positive score
pr.add("A", "C", 1) # add negative score

rating = pr.createRating()
```

## Notes
Check console outputs, ensure that eigen values are randomly distributed within 0..1 interval, they should not be too low.
Otherwise more likely the rating will be calculated incorrectly with it.

## Examples
`music_rating_*.py` - example applications that calculate the ranking of music artists based on how often they have influenced other artists.
`page_rank_class_test_negative_likes_1_5.py` - shows how to calculate ratings where scores 1 to 5 are applied instead of number likes
