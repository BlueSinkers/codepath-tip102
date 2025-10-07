"""
Questions I would ask:
1. should we treat text case-insensitive?
2. how to handle punctuation?
3. what if multiple words tie for max frequency?

Plan in plain english:
lowercase text, remove punctuation, split into words, count frequency of each word in a dictionary, find max frequency, return dictionary and list of word(s) with max frequency
"""

import string
def word_frequency_analysis(text):
 tr = str.maketrans('','',string.punctuation)
 t = text.lower().translate(tr)
 freq = {}
 for w in t.split(): freq[w] = freq.get(w,0)+1
 if freq:
  mf = max(freq.values())
  mc = [w for w,c in freq.items() if c==mf]
 else: mc = []
 return freq,mc

text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
print(word_frequency_analysis(text))

text_2 = "Digital nomads love to travel. Travel is their passion."
print(word_frequency_analysis(text_2))

text_3 = "Stay connected. Stay productive. Stay happy."
print(word_frequency_analysis(text_3))

#time complexity: O(n)
#space complexity: O(k)
