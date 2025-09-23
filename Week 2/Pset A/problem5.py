"""
Questions I would ask to help understand question:
1. How do I iterate through dictionary?
2. How do I track frequency?

Plan in plain English (pseudocode):
I will iterate through the dictionary keys and for each value, make a frequency map. I will then find the maximum value in the frequency map and return that.

Begin problem:
"""

def best_set(votes):
    tally = {}
    for voter, artist in votes.items():
        if artist not in tally:
            tally[artist] = 0
        tally[artist] += 1
    max_votes = max(tally.values())
    for artist, count in tally.items():
        if count == max_votes:
            return artist

#examples
votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))