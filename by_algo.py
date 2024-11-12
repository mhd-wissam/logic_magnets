from bfs import Bfs
from dfs import Dfs
from tree import Tree
class By_algo:
    def solve_algo(stage):
        node=Tree(stage)
        x=node.creat_tree()

        y=Dfs.dfs(x)
        #y=Bfs.bfs(x)
        if y != None :       
            stack=[]
            stack.append(y)

            while(stack[-1].parent !=None):
                stack.append(stack[-1].parent)
            print("solution:\n")
            while stack:
                top_element = stack[-1]
                stack.pop().value.display()
                print("\n")
        else:
            print("no solution")         