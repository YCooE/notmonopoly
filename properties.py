# Not used for current scope of project
# expandable if properties are put in random order
class Properties:
    def __init__(self, name, cost, color, owned, owner):
        self.name = name
        self.cost = cost
        self.color = color
        self.owned = owned
        self.owner = 'None'


    def purchase_card(self, player):
        if self.card_cost > player.balance:
            player.status = True
        else:
            player.properties.append(self)
            player.reduce(self.cost)
            self.owner = player

