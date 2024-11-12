from tree import Tree
from collections import deque
class Bfs:

    def bfs(node: Tree):
        queue = deque()
        visited = set()

        queue.append(node)
        visited.add(node)

        return Bfs.help(queue, visited)


    def help(queue, visited):
        if not queue:
            return None

        node = queue.popleft()

        if node.value.check_win():
            return node

        for child in node.children:
            if child not in visited:
                queue.append(child)
                visited.add(child)

                if child.value.check_win():
                    return child
                
        return Bfs.help(queue, visited)
        
