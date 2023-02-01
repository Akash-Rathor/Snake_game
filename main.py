from storage import Pointers
import random
import time
# from playsound import playsound


class Board:

    _count = 0

    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.board = self.__create_board()
        self.board[(0,0)] = '🐸'
    
    def __new__(cls,rows,cols):
        if cls._count>=1:
            raise Exception('Only one board can exist at a time')
        else:
            cls._count+=1
            return super(Board,cls).__new__(cls)

    def __create_board(self):
        y = {}
        for j in range(self.rows):
            for i in range(self.cols):
                y[(j,i)]='🥚'
        return y


class Snake(Pointers):

    _snake_count = 0
    _score = 0
    _plus_point = 50

    def __init__(self,boardObj):
        self.face = [0,0]
        self.length = 1
        self.boardObj = boardObj
        self.pointers = Pointers()
        self.fruit_loc = (random.randint(0,8),random.randint(0,8))
        self.boardObj.board[self.fruit_loc]='🍅'
        self.print_board()
        self.rightbtn = False
        self.upbtn = False
        self.downbtn = False
        self.leftbtn = False

    def __new__(cls,boardObj):
        if cls._snake_count>=1:
            raise Exception('Only One snake can exist in a game')
        else:
            cls._snake_count+=1
            return super(Snake,cls).__new__(cls)

        
    def add_fruit_random_location(self):
        exist = False
        while not exist:
            self.fruit_loc = (random.randint(0,8),random.randint(0,8))
            if self.boardObj.board[self.fruit_loc]=='🥚':
                exist = True
        self.boardObj.board[self.fruit_loc]='🍅'


    def add_point(self):
        self._score+=self._plus_point

    @property
    def right(self):
        # self.change_btn('right')
        # while self.rightbtn:
        self.boardObj.board[(self.face[0],self.face[1])]='🚙'
        self.face[1]+=1
        point = (self.face[0],self.face[1])
        if not self.check_if_fruit_taken(point):
            return f"Player out! total score {self._score}"
        time.sleep(1)

    @property
    def left(self):
        # self.change_btn('left')
        # while self.leftbtn:
        self.boardObj.board[(self.face[0],self.face[1])]='🚙'
        self.face[1]-=1
        point = (self.face[0],self.face[1])
        if not self.check_if_fruit_taken(point):
            return f"Player out! total score {self._score}"
        time.sleep(1)

    @property
    def up(self):
        # self.change_btn('up')
        # while self.upbtn:
        self.boardObj.board[(self.face[0],self.face[1])]='🚙'
        self.face[0]-=1
        point = (self.face[0],self.face[1])
        if not self.check_if_fruit_taken(point):
            return f"Player out! total score {self._score}"
        time.sleep(1)

    @property
    def down(self):
        # self.change_btn('down')
        # while self.downbtn:
        self.boardObj.board[(self.face[0],self.face[1])]='🚙'
        self.face[0]+=1
        point = (self.face[0],self.face[1])
        if not self.check_if_fruit_taken(point):
            return f"Player out! total score {self._score}"
        time.sleep(1)

    def check_if_fruit_taken(self,point):

        if self._check_boundary_touch:
            if self.boardObj.board[point]=='🍅':
                self.pointers.enqueue(point)
                self.boardObj.board[point]='🐸'
                self.add_fruit_random_location()
                self.add_point()
                self.print_board()
                return True
            else:
                self.boardObj.board[self.pointers.dequeue()]='🥚'
                if self.boardObj.board[point]!='🥚':
                    if self.boardObj.board[point]:
                        self.boardObj.board[point] = '💢'
                    self.print_board()
                    return False
                self.boardObj.board[point]='🐸'
                self.pointers.enqueue(point)
                self.print_board()
                return True
        return False

    def print_board(self):
        count = 0
        print('-'*(3*self.boardObj.rows)+'-')
        print('|',end='')
        for key,val in self.boardObj.board.items():
            count+=1
            print(val,end='|')
            if count%self.boardObj.cols==0:
                print()
                print('-'*(3*self.boardObj.rows)+'-')
                print('|',end='')
            

    def change_btn(self,btn):
        if btn=='right':
            self.rightbtn = True
            self.upbtn = False
            self.downbtn = False
            self.leftbtn = False
        if btn=='left':
            self.rightbtn = False
            self.upbtn = False
            self.downbtn = False
            self.leftbtn = True
        if btn=='up':
            self.rightbtn = False
            self.upbtn = True
            self.downbtn = False
            self.leftbtn = False
        if btn=='down':
            self.rightbtn = False
            self.upbtn = False
            self.downbtn = True
            self.leftbtn = False


    @property
    def _check_boundary_touch(self):
        if self.face[0]<0 or self.face[1]>=self.boardObj.rows or self.face[1]<0 or self.face[0]>=self.boardObj.cols:
            return False
        return True

        
game_board = Board(9,9)
player1 = Snake(game_board)
player1
            
