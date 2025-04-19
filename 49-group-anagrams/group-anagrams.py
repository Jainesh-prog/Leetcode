from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a default dictionary to map sorted words to list of anagrams
        anagram_map = defaultdict(list)

        # Loop through each word in the input list
        for word in strs:
            # Sort the word to form a key — anagrams will have the same sorted key
            sorted_word = ''.join(sorted(word))

            # Append the original word to the list corresponding to the sorted key
            anagram_map[sorted_word].append(word)

        # Return all values (lists of grouped anagrams) from the dictionary
        return list(anagram_map.values())
