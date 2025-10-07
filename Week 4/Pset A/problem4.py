"""
Questions I would ask:
1. What if the collection is empty? Should return 0.
2. Are all values guaranteed to be numbers?

Plan in plain English:
If collection is empty, return 0. Otherwise, sum all 'value' fields and divide by number of NFTs to get average.
"""

def average_nft_value(nft_collection):
    if not nft_collection:
        return 0
    total_value = sum(nft["value"] for nft in nft_collection)
    average = total_value / len(nft_collection)
    return average

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
print(average_nft_value(nft_collection_2))  # 9.15

# Time complexity: O(n)
# Space complexity: O(1)
