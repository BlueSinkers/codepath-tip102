"""
Questions I would ask to help understand question:
1. What if some NFT dictionaries don’t have a "name" key?
2. Can the collection be empty? What should be returned then?

Plan in plain English (pseudocode):
Create an empty list. Loop through each NFT in the collection. Extract the value of the "name" key and append to the list. Return the list at the end.
"""

def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]
print(extract_nft_names(nft_collection))  # ['Abstract Horizon', 'Pixel Dreams', 'Future City']

# Time complexity: O(n) 
# Space complexity: O(n) 
