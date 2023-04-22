from random import randint

dice = lambda :randint(1,6)

class Board:
    def __init__(self):
        self.move_of_col=0
        self.players=[Player(i) for i in range(4)]
        self.grid=[]
        self.update()
    def update(self):
        """
        first 52 cells are the runing path of board starting from red to red
        
        """
        grid=[[] for i in range(92)]
        for player in self.players:
            for pice in player.pices:
                index = self.pice_to_board_ind(pice)
                grid[index].append(pice)
        self.grid=grid

    def pice_to_board_ind(self,pice):
        # 0 to 4 are home cell for rispective
        if pice.is_at_home:
            return pice.identity+(4*pice.col)
        # elif pice.is_at_end:
        #     print("error 3")
        #     return len(self.grid)-(4-pice.col)
        # elif pice.dist_from_home>52:
        #     print("error 3")
        #     return (51-pice.dist_from_home)+52+(5*pice.col)
        # elif 0<pice.dist_from_home<52:return self.col_to_running_ind(pice)
        # else:print("error in pice_to_board_ind")
    def col_to_running_ind(self,pice):
        val=pice.dist_from_home+(pice.col*13)
        if val>52:return val-52
        return val

class Pice:
    def __init__(self,col,identity):
        self.is_at_home=True
        self.is_at_rest=True
        self.is_at_end=False
        self.identity=identity
        self.col=col
        self.dist_from_home=0

class Player:
    def __init__(self,col):
        self.col=col
        self.pices=[Pice(self.col,i) for i in range(4)]