from tree import Tree

class Dfs:

    def dfs(node: Tree):
        stack = [node]
        visited = set()

        visited.add(node)

        return Dfs.help(stack, visited)


    def help(stack, visited):
        if not stack:
            return None
        node=stack.pop()
        if node.value.check_win():
            return node
        for child in node.children:
            if child not in visited:
                stack.append(child)
                visited.add(child)
                if node.value.check_win():
                    return node
                
        return Dfs.help(stack, visited)


    