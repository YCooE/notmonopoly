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
    
    def position_execution(self, board, own_status, owner_name, scope):

        if self.position >  8:
            self.position = self.position % 9
            self.balance += 1

        board_space = board[self.position]
        print(f"Player {self.name} turn")
        print(f"Player {self.name} has {self.balance}")
        print(f"You are on {board_space['name']}, position {self.position}")
        # Double charge boolean flag, passed to charge
        double_charge = False
        # if status of owner is set to False
        # Forced to buy property
        if own_status[self.position] == False:
            self.reduce(board_space['price'])
            own_status[self.position] = True
            owner_name[self.position] = self.name
        # if property is owned and it is a property under someone elses name
        elif own_status[self.position] == True and board_space['type'] == 'property' and self.name != eval(owner_name[self.position], scope):
            # check if property owner also owns the neighbour color property
            # if he does charge twice amount, flag passed to charge
            if self.position == 1 or 2 and owner_name[1] == owner_name[2]:
                double_charge = True
            elif self.position == 3 or 4 and owner_name[3] == owner_name[4]:
                double_charge = True
            elif self.position == 5 or 6 and owner_name[5] == owner_name[6]:
                double_charge = True
            elif self.position == 7 or 8 and owner_name[7] == owner_name[8]:
                double_charge = True
            
            self.charge(board_space, owner_name, scope, double_charge)


    def add(self, amount):

        self.balance += amount
    
    def reduce(self, amount):
        self.balance -= amount
        # checks if balance is possible, 
        # if impossible still buys but gets deleted
        if self.balance < 0:
            self.status = True

    def charge(self, property, owner_name, scope, double_charge):
        if double_charge == True:
            cost = property['price']*2
        else:
            cost = property['price']

        self.reduce(cost)

        eval(owner_name[self.position], scope).add(cost)
    