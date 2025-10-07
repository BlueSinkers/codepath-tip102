"""
Questions I would ask:
1. Can NFTs have empty 'tags' list? Should they be ignored?
2. Can collections be empty?

Plan in plain English:
Create an empty list. Loop through each collection, then each NFT. If the tag is in nft['tags'], append nft['name'] to result. Return result at the end.
"""

def search_nft_by_tag(nft_collections, tag):
    result = []
    for collection in nft_collections:
        for nft in collection:
            if tag in nft.get("tags", []):
                result.append(nft["name"])
    return result

nft_collections = [
    [
        {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
        {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
    ],
    [
        {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
        {"name": "City Lights", "tags": ["modern", "landscape"]}
    ]
]
print(search_nft_by_tag(nft_collections, "landscape"))  # ['Urban Jungle', 'City Lights']

# Time complexity: O(n) 
# Space complexity: O(m)
