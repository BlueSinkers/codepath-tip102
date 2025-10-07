"""
Questions I would ask:
1. How do we define a popular creator? Only if they have more than one NFT?
2. Can the collection be empty?

Plan in plain English:
Use a dictionary to count how many NFTs each creator has. Then, loop through the dictionary and pick creators with count > 1. Return those creators as a list.
"""

def identify_popular_creators(nft_collection):
    creator_count = {}
    for nft in nft_collection:
        creator = nft["creator"]
        creator_count[creator] = creator_count.get(creator, 0) + 1
    
    popular_creators = [creator for creator, count in creator_count.items() if count > 1]
    return popular_creators

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
print(identify_popular_creators(nft_collection))  # ['ArtByAlex']

# Time complexity: O(n) 
# Space complexity: O(k),  k = number of unique creators
   