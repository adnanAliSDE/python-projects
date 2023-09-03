"""Adding score logic"""

import pickle

score = 0

user = "adnann30777"
# user = ("Enter your username: ")

scores = {}

with open("scores.dat", "rb") as f:
    scores = pickle.load(f)

print(scores)
