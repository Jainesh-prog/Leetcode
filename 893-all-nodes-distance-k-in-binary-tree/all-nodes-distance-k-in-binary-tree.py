from collections import defaultdict, deque

class Solution:
    def distanceK(self, root, target, K):
        graph = defaultdict(list)

        # Step 1: Build the graph
        def buildGraph(node, parent=None):
            if not node:
                return
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            buildGraph(node.left, node)
            buildGraph(node.right, node)

        buildGraph(root)

        # Step 2: BFS from the target node
        visited = set()
        queue = deque()
        queue.append((target.val, 0))
        visited.add(target.val)

        res = []

        while queue:
            node, dist = queue.popleft()

            if dist == K:
                res.append(node)

            elif dist < K:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))

        return res
