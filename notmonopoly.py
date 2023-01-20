import json

import playerdef as p_init

board_file = open('board.json')
roll_file1 = open('rolls_1.json')

data = json.load(board_file)

rolls1 = json.load(roll_file1)

Peter = p_init.Player("Peter", 16, 0, [], True)
Billy = p_init.Player("Billy", 16, 0, [], True)
Charlotte = p_init.Player("Charlotte", 16, 0, [], True)
Sweedal = p_init.Player("Sweedal", 16, 0, [], True)

p_list = [Peter, Billy, Charlotte, Sweedal]



for i in data:
    print(i)

print(data[1]['name'])

for i in range(len(rolls1)):
    Peter.move(rolls1[i])
    Peter.position_execution(data)
    print(Peter.position)

print(Peter.position)