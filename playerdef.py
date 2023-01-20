class Player:
    def __init__(self, name, balance, position, properties, status):
        self.name = name             # string
        self.balance = balance       # int
        self.position = position     # int
        self.properties = properties # []
        self.status = status         # bool Whether they have lost due to insufficient funds
    
    def move(self, spaces):
        self.position += spaces
        return self.position
    
    def position_execution(self, board, own_status, owner_name):

        if self.position > 8:
            self.position = self.position % 9
            self.balance += 1

        board_space = board[self.position]

        print(f"You are on {board_space['name']}, position {self.position}")

        if own_status[self.position] == False:
            self.balance -= board_space['price']
            own_status[self.position] = True
            owner_name[self.position] = self.name
        elif board_space['type'] == 'property':
            #self.charge(board_space, owner_name)

            eval(owner_name[self.position]).balance += board_space['price']


    def add(self, amount):

        self.balance += amount
    
    def reduce(self, amount):

        self.balance -= amount
        if self.balance < 0:
            self.status = True

    def charge(self, property, owner_name):
        cost = property['price']

        self.reduce(cost)

        eval(owner_name[self.position]).add(cost)
    