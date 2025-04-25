class Solution:

    def ladderLength(self,beginWord, endWord, wordList):
        # If endWord is not in the list, there's no valid transformation
        if endWord not in wordList:
            return 0

        L = len(beginWord)  # All words are of same length
        graph = defaultdict(list)  # Pattern map: pattern -> list of words

        # Preprocess: For every word in wordList, create L wildcard patterns
        for word in wordList:
            for i in range(L):
                # Replace one character with '*' to create pattern
                pattern = word[:i] + "*" + word[i+1:]
                graph[pattern].append(word)

        # Queue for BFS, initialized with (current_word, current_level)
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])  # To avoid revisiting same word

        while queue:
            current_word, level = queue.popleft()

            # Generate all wildcard patterns for current word
            for i in range(L):
                pattern = current_word[:i] + "*" + current_word[i+1:]

                # All words that share this pattern are 1 letter away
                for neighbor in graph[pattern]:
                    if neighbor == endWord:
                        return level + 1  # Reached the end, return steps

                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))

                # Optional: clear list to avoid redundant checks later
                graph[pattern] = []

        # No valid path found
        return 0
