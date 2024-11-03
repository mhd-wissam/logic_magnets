from board import Board
from cell import Cell
from stone import Stone
from stage import Stage
from bfs import TreeNode1
if __name__ == "__main__":

    
    stage = int(input("pleas enter number of stage from 1 to 25: "))
    stage-=1
    Stage.stage_array[stage].display()

    for i in range(1, Stage.stage_array[stage].step):
        print("to move put")
        from_x=int(input("from x:"))
        from_y=int(input("from y:"))

        print("where do you want move it")
        to_x=int(input("to x:"))
        to_y=int(input("to y:"))
        ss=Stage.stage_array[stage].move_stone(from_x,from_y,to_x,to_y)
        # ss.display()
        if Stage.stage_array[stage].check_win() :
            break