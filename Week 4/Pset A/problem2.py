"""
Questions I would ask:
1. What happens if we use '+=' on a string? Does it append the string or characters individually?
2. Should we handle empty collections?

Plan in plain English:
The bug is using '+=' which adds each character of the string instead of the whole string. Fix by using append() instead of '+='.
"""

def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]
print(extract_nft_names(nft_collection_2))  # ['Golden Hour']

nft_collection_3 = []
print(extract_nft_names(nft_collection_3))  # []

