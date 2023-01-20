class Player:
    def __init__(self, name, balance, position, properties, status):
        self.name = name             # string
        self.balance = balance       # int
        self.position = position     # int
        self.properties = properties # []
        self.status = status         # bool
    
    def move(self, spaces):
        self.position += spaces
        return self.position
    
    def position_execution(self, board):

        if self.position > 8:
            self.position = self.position % 8
            self.balance += 1

        board_space = board[self.position]

        print(f"You are on {board_space['name']}")

        #return 0


    
