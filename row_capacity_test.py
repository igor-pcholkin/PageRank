from page_rank import getMaxRowLikeCapacity

assert getMaxRowLikeCapacity({ "A": { "B": 4, "D": 3 }, "B": { "C": 8 } }) == -1
assert getMaxRowLikeCapacity({ "A": { "B": 4, "D": 4 }, "B": { "C": 7 } }) == -1
assert getMaxRowLikeCapacity({ "A": { "B": 4, "D": 4 }, "B": { "C": 8 } }) == 8
assert getMaxRowLikeCapacity({ "A": { "B": 0, "D": 0 }, "B": { "C": 0 } }) == 0
