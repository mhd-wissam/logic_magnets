from board import Board
import copy
class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None  # Add a parent attribute

    def add_child(self, child_node):
        child_node.parent = self  # Set the parent of the child node to the current node
        self.children.append(child_node)

    def get_parent(self):
        return self.parent  # Return the parent of the current node

    def creat_tree(self):
        if self.value.step ==0 :
            return
        magnets = []
        xp = self.value.find_x("+")
        yp = self.value.find_y("+")
        xn = self.value.find_x("-")
        yn = self.value.find_y("-")

        if xn is not None:
            magnets.append('-')  # Add - if found

        if xp is not None:
            magnets.append('+')  # Add + if found
            
        for magnet in magnets:
            if magnet == '+':
                x = xp
                y = yp
            elif magnet == '-':
                x = xn
                y = yn

            for i in range(self.value.size):
                for j in range(self.value.size):
                            if self.value.grid[i][j].is_empty and self.value.grid[i][j].cell_type !="block":

                                child=self.value.move_stone(x,y,i,j)
                                # if child not in v :
                                child_node = Tree(child)
                                self.add_child(child_node)
                                # v.append(child)
                                # child.display()
                                child_node.creat_tree()
                    
        return self

    def chiled_of_child(self):
        for i in range(len(self.children)):
            x = self.children[i]
            x.creat_tree()
            # x.value.display()      