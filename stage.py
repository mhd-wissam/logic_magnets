from board import Board
from cell import Cell
from stone import Stone
import random
import string
class Stage:

    positive_stone = Stone('+')
    negative_stone = Stone('-')
    iron_stone = Stone('f')
    stage_array=[]

    board1 = Board(size=4, step=3)

    stage_array.append(board1)
    # Place block and goal cells
    board1.place_cell(3, 0, 'block')
    board1.place_cell(3, 1, 'block')
    board1.place_cell(3, 2, 'block') 
    board1.place_cell(3, 3, 'block')
   
    board1.place_cell(1, 1, 'goal')
    board1.place_cell(1, 3, 'goal')

    # Place stones
    board1.place_stone(2, 0, positive_stone)
    board1.place_stone(1, 2, iron_stone)
#........................................................................

    board2 = Board(5,1)
    stage_array.append(board2)
    # Plae block and goal cells
    board2.place_cell(0, 2, 'goal')
    board2.place_cell(2, 0, 'goal') 
    board2.place_cell(2, 2, 'goal')
    board2.place_cell(2, 4, 'goal')
    board2.place_cell(4, 2, 'goal')

    # Place stones
    board2.place_stone(4, 0, positive_stone)
    board2.place_stone(1, 2, iron_stone)
    board2.place_stone(2, 1, iron_stone)
    board2.place_stone(2, 3, iron_stone)
    board2.place_stone(3, 2, iron_stone)

#.................................................................

    board3 = Board(4,2)
    stage_array.append(board3)
    # Plae block and goal cells
    board3.place_cell(0, 0, 'block')
    board3.place_cell(0, 1, 'block')
    board3.place_cell(0, 2, 'block')
    board3.place_cell(3, 0, 'block')
    board3.place_cell(3, 1, 'block')
    board3.place_cell(3, 2, 'block')
    board3.place_cell(3, 3, 'block')

    board3.place_cell(0, 3, 'goal')
    board3.place_cell(2, 3, 'goal') 

    # Place stones
    board3.place_stone(2, 0, positive_stone)
    board3.place_stone(1, 2, iron_stone)

#.................................................................

    board4 = Board(5,2)
    stage_array.append(board4)
    # Plae block and goal cells
    board4.place_cell(0, 0, 'block')
    board4.place_cell(1, 0, 'block')
    board4.place_cell(2, 0, 'block')
    board4.place_cell(3, 0, 'block')
    board4.place_cell(4, 0, 'block')
    board4.place_cell(0, 1, 'block')
    board4.place_cell(1, 1, 'block')
    board4.place_cell(2, 1, 'block')
    board4.place_cell(3, 1, 'block')
    board4.place_cell(4, 1, 'block')
    board4.place_cell(1, 2, 'block')
    board4.place_cell(3, 2, 'block')

    board4.place_cell(0, 2, 'goal')
    board4.place_cell(0, 4, 'goal') 
    board4.place_cell(4, 3, 'goal') 
    # Place stones
    board4.place_stone(2, 2, positive_stone)
    board4.place_stone(1, 3, iron_stone)
    board4.place_stone(3, 3, iron_stone)

#..............................................................

    board5 = Board(4,2)
    stage_array.append(board5)
    # Plae block and goal cells
    board5.place_cell(0, 0, 'block')
    board5.place_cell(1, 0, 'block')
    board5.place_cell(2, 0, 'block')
    board5.place_cell(3, 0, 'block')
    board5.place_cell(0, 2, 'block')
    board5.place_cell(1, 2, 'block')
    board5.place_cell(2, 2, 'block')

    board5.place_cell(0, 1, 'goal')
    board5.place_cell(0, 3, 'goal') 
    board5.place_cell(1, 1, 'goal') 
    board5.place_cell(1, 3, 'goal') 
    board5.place_cell(3, 1, 'goal') 

    # Place stones
    board5.place_stone(3, 2, positive_stone)
    board5.place_stone(1, 1, iron_stone)
    board5.place_stone(1, 3, iron_stone)
    board5.place_stone(2, 1, iron_stone)
    board5.place_stone(2, 3, iron_stone)

    #......................................................

    board6 = Board(5,2)
    stage_array.append(board6)
    # Plae block and goal cells
    board6.place_cell(3, 0, 'block')
    board6.place_cell(3, 1, 'block')
    board6.place_cell(3, 2, 'block')
    board6.place_cell(3, 3, 'block')
    board6.place_cell(3, 4, 'block')
    board6.place_cell(4, 0, 'block')
    board6.place_cell(4, 1, 'block')
    board6.place_cell(4, 2, 'block')
    board6.place_cell(4, 3, 'block')
    board6.place_cell(4, 4, 'block')

    board6.place_cell(0, 3, 'goal') 
    board6.place_cell(1, 2, 'goal') 
    board6.place_cell(2, 3, 'goal') 


    # Place stones
    board6.place_stone(2, 0, positive_stone)
    board6.place_stone(1, 1, iron_stone)
    board6.place_stone(1, 3, iron_stone)

    #solve
    # Stage.board6.move_stone(2, 0,1, 0)
    # Stage.board6.move_stone(1, 0, 2, 3)

    #......................................................

    board7 = Board(5,2)
    stage_array.append(board7)

    # Plae block and goal cells
   
    board7.place_cell(0, 0, 'block')
    board7.place_cell(1, 0, 'block')
    board7.place_cell(2, 0, 'block')
    board7.place_cell(3, 0, 'block')
    board7.place_cell(4, 0, 'block')
    board7.place_cell(4, 1, 'block')
    board7.place_cell(4, 2, 'block')
    board7.place_cell(4, 3, 'block')

    board7.place_cell(0, 1, 'goal') 
    board7.place_cell(1, 1, 'goal') 
    board7.place_cell(2, 4, 'goal')  
    board7.place_cell(3, 3, 'goal')  
    board7.place_cell(4, 4, 'goal')  


    # Place stones
    board7.place_stone(2, 2, positive_stone)
    board7.place_stone(1, 1, iron_stone)
    board7.place_stone(2, 1, iron_stone)
    board7.place_stone(3, 2, iron_stone)
    board7.place_stone(3, 3, iron_stone)

    # solve
    # Stage.board7.move_stone(2, 2,3, 1)
    # Stage.board7.move_stone(3, 1,4, 4)

    #......................................................
    board8 = Board(4, 2)
    stage_array.append(board8)

    # Place goal cells
    board8.place_cell(3, 0, 'block')
    board8.place_cell(3, 1, 'block')
    board8.place_cell(3, 2, 'block')
    board8.place_cell(3, 3, 'block')

    board8.place_cell(0, 0, 'goal')
    board8.place_cell(0, 2, 'goal')
    board8.place_cell(2, 2, 'goal')

    # Place stones
    board8.place_stone(2, 0, positive_stone)
    board8.place_stone(1, 1, iron_stone)
    board8.place_stone(1, 2, iron_stone)
    
    #.......................................................

    board9 = Board(7, 2)
    stage_array.append(board9)

    # Place goal cells
    for i in range(1, 7):
        for j in range(0, 7):
            board9.place_cell(i, j, 'block')

    board9.place_cell(0, 1, 'goal')
    board9.place_cell(0, 3, 'goal')
    board9.place_cell(0, 6, 'goal')

    # Place stones

    board9.place_stone(0, 0, positive_stone)
    board9.place_stone(0, 3, iron_stone)
    board9.place_stone(0, 5, iron_stone)

    # Adjust positions based on the exact board layout you need

#...................................................................

    board10 = Board(4,2)
    stage_array.append(board10)

    # Plae block and goal cells
    board10.place_cell(1, 1, 'goal')
    board10.place_cell(1, 3, 'goal') 
    board10.place_cell(3, 3, 'goal') 
    board10.place_cell(3, 0, 'goal') 

    # Place stones
    board10.place_stone(0, 0, positive_stone)
    board10.place_stone(2, 2, iron_stone)
    board10.place_stone(2, 3, iron_stone)
    board10.place_stone(3, 1, iron_stone)

#...................................................................

    board11 = Board(5, 1)
    stage_array.append(board11)

    # Place goal cells
    for i in range(1, 5):
        for j in range(0, 5):
            board11.place_cell(i, j, 'block')

    board11.place_cell(1, 2, 'normal')
    board11.place_cell(0, 1, 'goal')
    board11.place_cell(0, 2, 'goal')
    board11.place_cell(0, 3, 'goal')

    # Place stones

    board11.place_stone(1, 2, negative_stone)
    board11.place_stone(0, 0, iron_stone)
    board11.place_stone(0, 4, iron_stone)
#....................................................................

    board12 = Board(5, 1)
    stage_array.append(board12)

    # Place goal cells
    board12.place_cell(0, 2, 'block')
    board12.place_cell(0, 3, 'block')
    board12.place_cell(1, 2, 'block')
    board12.place_cell(1, 3, 'block')
    board12.place_cell(0, 4, 'block')
    board12.place_cell(1, 4, 'block')
    board12.place_cell(2, 4, 'block')
    board12.place_cell(3, 4, 'block')
    board12.place_cell(4, 4, 'block')

    board12.place_cell(1, 0, 'goal')
    board12.place_cell(2, 0, 'goal')
    board12.place_cell(4, 0, 'goal')
    board12.place_cell(4, 2, 'goal')

    # Place stones
    board12.place_stone(3, 1, negative_stone)
    board12.place_stone(0, 0, iron_stone)
    board12.place_stone(1, 0, iron_stone)
    board12.place_stone(4, 3, iron_stone)
#...................................................................

    board13 = Board(6, 2)
    stage_array.append(board13)

    # Place goal cells
    board13.place_cell(1, 0, 'block')
    board13.place_cell(1, 4, 'block')
    board13.place_cell(1, 5, 'block')
    board13.place_cell(2, 0, 'block')
    board13.place_cell(2, 4, 'block')
    board13.place_cell(2, 5, 'block')
    board13.place_cell(3, 0, 'block')
    board13.place_cell(3, 1, 'block')
    board13.place_cell(3, 2, 'block')
    board13.place_cell(3, 3, 'block')
    board13.place_cell(3, 4, 'block')
    board13.place_cell(3, 5, 'block')
    board13.place_cell(4, 0, 'block')
    board13.place_cell(4, 1, 'block')
    board13.place_cell(4, 2, 'block')
    board13.place_cell(4, 3, 'block')
    board13.place_cell(4, 4, 'block')
    board13.place_cell(4, 5, 'block')
    board13.place_cell(5, 0, 'block')
    board13.place_cell(5, 1, 'block')
    board13.place_cell(5, 2, 'block')
    board13.place_cell(5, 3, 'block')
    board13.place_cell(5, 4, 'block')
    board13.place_cell(5, 5, 'block')

    board13.place_cell(0, 3, 'goal')
    board13.place_cell(0, 4, 'goal')
    board13.place_cell(1, 1, 'goal')
    board13.place_cell(2, 1, 'goal')

    # Place stones
    board13.place_stone(2, 3, negative_stone)
    board13.place_stone(0, 0, iron_stone)
    board13.place_stone(0, 4, iron_stone)
    board13.place_stone(0, 5, iron_stone)
#...................................................................

    board14 = Board(4,2)
    stage_array.append(board14)

    # Plae block and goal cells
    board14.place_cell(1, 0, 'goal')
    board14.place_cell(1, 2, 'goal') 
    board14.place_cell(2, 1, 'goal') 
    board14.place_cell(2, 2, 'goal') 

    # Place stones
    board14.place_stone(3, 3, negative_stone)
    board14.place_stone(0, 3, iron_stone)
    board14.place_stone(2, 0, iron_stone)
    board14.place_stone(3, 0, iron_stone)
#...................................................................

    board15 = Board(5, 2)
    stage_array.append(board15)

    # Place goal cells
    board15.place_cell(3, 0, 'block')
    board15.place_cell(3, 1, 'block')
    board15.place_cell(3, 2, 'block')
    board15.place_cell(3, 3, 'block')
    board15.place_cell(3, 4, 'block')
    board15.place_cell(4, 0, 'block')
    board15.place_cell(4, 1, 'block')
    board15.place_cell(4, 2, 'block')
    board15.place_cell(4, 3, 'block')
    board15.place_cell(4, 4, 'block')

    board15.place_cell(0, 0, 'goal')
    board15.place_cell(0, 2, 'goal')
    board15.place_cell(1, 4, 'goal')
    board15.place_cell(2, 4, 'goal')

    # Place stones
    board15.place_stone(2, 2, negative_stone)
    board15.place_stone(1, 2, positive_stone)
    board15.place_stone(0, 1, iron_stone)
    board15.place_stone(0, 3, iron_stone)

#...................................................................

    board16 = Board(5, 3)
    stage_array.append(board16)

    board16.place_cell(0, 3, 'goal')
    board16.place_cell(0, 4, 'goal')
    board16.place_cell(4, 0, 'goal')
    board16.place_cell(4, 3, 'goal')
     # Place stones
    board16.place_stone(2, 0, negative_stone)
    board16.place_stone(2, 4, positive_stone)
    board16.place_stone(1, 2, iron_stone)
    board16.place_stone(3, 2, iron_stone)
#...................................................................
#...................................................................

    board17 = Board(4, 2)
    stage_array.append(board17)

    board17.place_cell(1, 1, 'goal')
    board17.place_cell(1, 3, 'goal')
    board17.place_cell(2, 2, 'goal')
    board17.place_cell(3, 1, 'goal')
     # Place stones
    board17.place_stone(0, 0, negative_stone)
    board17.place_stone(3, 3, positive_stone)
    board17.place_stone(0, 2, iron_stone)
    board17.place_stone(2, 0, iron_stone)
#...................................................................
#...................................................................

    board18 = Board(6, 2)
    stage_array.append(board18)

   # Place goal cells
    board18.place_cell(0, 0, 'block')
    board18.place_cell(0, 1, 'block')
    board18.place_cell(0, 4, 'block')
    board18.place_cell(0, 5, 'block')
    board18.place_cell(1, 0, 'block')
    board18.place_cell(1, 1, 'block')
    board18.place_cell(1, 4, 'block')
    board18.place_cell(1, 5, 'block')
    board18.place_cell(4, 0, 'block')
    board18.place_cell(4, 1, 'block')
    board18.place_cell(4, 4, 'block')
    board18.place_cell(4, 5, 'block')
    board18.place_cell(5, 0, 'block')
    board18.place_cell(5, 1, 'block')
    board18.place_cell(5, 2, 'block') 
    board18.place_cell(5, 3, 'block')
    board18.place_cell(5, 4, 'block')
    board18.place_cell(5, 5, 'block')

    board18.place_cell(1, 3, 'goal')
    board18.place_cell(2, 1, 'goal')
    board18.place_cell(2, 2, 'goal')
    board18.place_cell(2, 3, 'goal')

    # Place stones
    board18.place_stone(4, 2, negative_stone)
    board18.place_stone(4, 3, positive_stone)
    board18.place_stone(0, 3, iron_stone)
    board18.place_stone(2, 0, iron_stone)
    board18.place_stone(2, 5, iron_stone)
#...................................................................
#...................................................................

    board19 = Board(5, 4)
    stage_array.append(board19)

   # Place goal cells
    board19.place_cell(0, 0, 'block')
    board19.place_cell(0, 4, 'block')
    board19.place_cell(2, 0, 'block')
    board19.place_cell(2, 4, 'block')
    board19.place_cell(4, 0, 'block')
    board19.place_cell(4, 4, 'block')
    

    board19.place_cell(1, 0, 'goal')
    board19.place_cell(1, 4, 'goal')
    board19.place_cell(2, 1, 'goal')
    board19.place_cell(3, 0, 'goal')
    board19.place_cell(3, 2, 'goal')
    board19.place_cell(3, 4, 'goal')



    # Place stones
    board19.place_stone(2, 2, negative_stone)
    board19.place_stone(0, 2, positive_stone)
    board19.place_stone(0, 3, iron_stone)
    board19.place_stone(0, 1, iron_stone)
    board19.place_stone(4, 1, iron_stone)
    board19.place_stone(4, 3, iron_stone)
#...................................................................
#...................................................................

    board20 = Board(5, 2)
    stage_array.append(board20)

   # Place goal cells
    board20.place_cell(0, 4, 'block')
    board20.place_cell(1, 4, 'block')
    board20.place_cell(2, 4, 'block')
    board20.place_cell(3, 4, 'block')
    board20.place_cell(4, 4, 'block')
    board20.place_cell(0, 3, 'goal')
    board20.place_cell(1, 0, 'goal')
    board20.place_cell(2 ,0, 'goal')
    board20.place_cell(3, 0, 'goal')
    # Pla20 stones
    board20.place_stone(4, 3, negative_stone)
    board20.place_stone(4, 2, positive_stone)
    board20.place_stone(0, 2, iron_stone)
    board20.place_stone(0, 1, iron_stone)
    board20.place_stone(4, 0, iron_stone)
    
#...................................................................
#...................................................................

    board21 = Board(4, 2)
    stage_array.append(board21)

   # Place goal cells
    board21.place_cell(3, 0, 'block')
    board21.place_cell(3, 1, 'block')
    board21.place_cell(3, 2, 'block')
    board21.place_cell(3, 3, 'block')
    board21.place_cell(0, 2, 'goal')
    board21.place_cell(1, 0, 'goal')
    board21.place_cell(2 ,1, 'goal')

    # Pla21 stones
    board21.place_stone(2, 3, negative_stone)
    board21.place_stone(2, 0, positive_stone)
    board21.place_stone(0, 1, iron_stone)
    board21.place_stone(1,1, iron_stone)
    board21.place_stone(1,2, iron_stone)
    
#...................................................................
    board22 = Board(5,3)
    stage_array.append(board22)
    board22.place_cell(0, 2, 'block')
    board22.place_cell(1, 2, 'block')
    board22.place_cell(3, 4, 'block')
    board22.place_cell(4, 0, 'block')
    board22.place_cell(4, 1, 'block')
    board22.place_cell(4, 2, 'block')
    board22.place_cell(4, 3, 'block')
    board22.place_cell(4, 4, 'block')

    board22.place_cell(0, 1, 'goal')
    board22.place_cell(0, 3, 'goal')
    board22.place_cell(1, 0, 'goal')
    board22.place_cell(1, 4, 'goal')
    board22.place_cell(2 ,1, 'goal')

    board22.place_stone(0, 0, positive_stone)
    board22.place_stone(3, 2, negative_stone)
    board22.place_stone(0, 3, iron_stone)
    board22.place_stone(0, 4, iron_stone)
    board22.place_stone(3, 0, iron_stone)

#...................................................................
    board23 = Board(5,3)
    stage_array.append(board23)
    board23.place_cell(4, 0, 'block')
    board23.place_cell(4, 1, 'block')
    board23.place_cell(4, 2, 'block')
    board23.place_cell(4, 3, 'block')
    board23.place_cell(4, 4, 'block')

    board23.place_cell(0, 2, 'goal')
    board23.place_cell(2, 1, 'goal')
    board23.place_cell(2, 2, 'goal')
    board23.place_cell(2, 3, 'goal')
    board23.place_cell(3 ,2, 'goal')

    board23.place_stone(3, 4, positive_stone)
    board23.place_stone(3, 2, negative_stone)
    board23.place_stone(0, 3, iron_stone)
    board23.place_stone(1, 4, iron_stone)
    board23.place_stone(2, 0, iron_stone)
#...................................................................

    board24 = Board(5,3)
    stage_array.append(board24)
    board24.place_cell(4, 0, 'block')
    board24.place_cell(4, 4, 'block')

    board24.place_cell(0, 3, 'goal')
    board24.place_cell(2, 1, 'goal')
    board24.place_cell(2, 3, 'goal')
    board24.place_cell(4, 1, 'goal')
    board24.place_cell(4 ,2, 'goal')

    board24.place_stone(1, 4, positive_stone)
    board24.place_stone(3, 0, negative_stone)
    board24.place_stone(0, 1, iron_stone)
    board24.place_stone(1, 3, iron_stone)
    board24.place_stone(3, 4, iron_stone)
#...................................................................

    board25 = Board(5,3)
    stage_array.append(board25)

    # Plae block and goal cells
    board25.place_cell(0, 4, 'block')
    board25.place_cell(1, 4, 'block')
    board25.place_cell(2, 4, 'block')
    board25.place_cell(3, 4, 'block')
    board25.place_cell(4, 4, 'block')

    board25.place_cell(0, 0, 'goal')
    board25.place_cell(0, 3, 'goal') 
    board25.place_cell(2, 0, 'goal') 
    board25.place_cell(4, 0, 'goal') 
    board25.place_cell(4, 1, 'goal') 
    board25.place_cell(4, 2, 'goal') 

    # Place stones
    board25.place_stone(4, 0, positive_stone)
    board25.place_stone(0, 3, negative_stone)
    board25.place_stone(0, 0, iron_stone)
    board25.place_stone(1, 2, iron_stone)
    board25.place_stone(3, 2, iron_stone)
    board25.place_stone(4, 3, iron_stone)

    # solve
    # Stage.board25.move_stone(4, 0,2, 2)
    # Stage.board25.move_stone(0, 3, 4, 0)
    # Stage.board25.move_stone(2, 2, 0, 0)

    #.................................................

    board26 = Board(5,3)
    stage_array.append(board26)
    board26.place_cell(0, 2, 'block')
    board26.place_cell(1, 2, 'block')
    board26.place_cell(2, 2, 'block')
    board26.place_cell(4, 0, 'block')
    board26.place_cell(4, 1, 'block')
    board26.place_cell(4, 2, 'block')
    board26.place_cell(4, 3, 'block')
    board26.place_cell(4, 4, 'block')

    board26.place_cell(0, 0, 'goal')
    board26.place_cell(3, 0, 'goal')
    board26.place_cell(3, 2, 'goal')
    board26.place_cell(3, 3, 'goal')

    board26.place_stone(1, 0, positive_stone)
    board26.place_stone(3, 0, negative_stone)
    board26.place_stone(1, 1, iron_stone)
    board26.place_stone(2, 3, iron_stone)
#...................................................................
    rand_num = random.randint(3, 5)
    rand_num1 = random.randint(1, 4)
    xm = random.randint(0, rand_num - 1)
    ym = random.randint(0, rand_num - 1)
    magnets = Stone(random.choice('+-'))
    board27 = Board(rand_num, rand_num1)
    stage_array.append(board27)
    board27.place_stone(xm, ym, magnets)

    goal_and_iron=random.randint(1, 4)
    for c in range(goal_and_iron):
        x = random.randint(0, rand_num - 1)
        y = random.randint(0, rand_num - 1)
        # Ensure x and y are not equal to xm and ym
        while x == xm and y == ym:
            x = random.randint(0, rand_num - 1)
            y = random.randint(0, rand_num - 1)

        board27.place_stone(x, y, iron_stone)

    for c in range(goal_and_iron+1):
        x=random.randint(0, rand_num-1)
        y=random.randint(0, rand_num-1)
        board27.place_cell(x, y, 'goal')



#....................................................................

    board28= Board(2,1)
    stage_array.append(board28)
    board28.place_stone(0, 0, positive_stone)
    board28.place_cell(1, 1, 'goal')
    board28.place_cell(0, 1, 'goal')