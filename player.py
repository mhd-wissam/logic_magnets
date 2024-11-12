from board import Board
from stage import Stage
from by_algo import By_algo
class Player:
    def my_self():
        num_stage = int(input("pleas enter number of stage from 1 to 25: "))
        num_stage-=1
        stage=Stage.stage_array[num_stage]
        stage.display()

        mm = int(input("If you want to play the game, choose 1, but if you want the solution directly, choose 2: "))

        if mm==1:
            for i in range(1,stage.step+1):

                xp = stage.find_x("+")
                yp = stage.find_y("+")
                xn = stage.find_x("-")
                yn = stage.find_y("-")

                if xp is not None:
                    print("to move + chose 1 ")

                if xn is not None:
                    print("to move - chose 2 ")

                while True:
                    mm = int(input(": "))
                    if mm in [1, 2]:
                        if mm == 2:
                            from_x = xn
                            from_y = yn
                            break
                        elif mm == 1:
                            from_x = xp
                            from_y = yp
                            break
                    else:
                        print("Invalid input. Please enter 1 or 2.")

                print("where do you want move it")
                to_x=int(input("to x:"))
                to_y=int(input("to y:"))
                print("..................................................")   
                stage=stage.move_stone(from_x,from_y,to_x,to_y)
                stage.display()
                if stage.check_win():
                    print("congratulations you win :) ")
                    break
                if stage.step==0:
                    print("you loser :(")

                print("..................................................")    
        else:
            By_algo.solve_algo(stage)