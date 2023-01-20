import json

import playerdef as p_init

board_file = open('board.json')
roll_file1 = open('rolls_1.json')

data = json.load(board_file)

rolls1 = json.load(roll_file1)

Peter = p_init.Player("Peter", 16, 0, [], False)
Billy = p_init.Player("Billy", 16, 0, [], False)
Charlotte = p_init.Player("Charlotte", 16, 0, [], False)
Sweedal = p_init.Player("Sweedal", 16, 0, [], False)

p_list = [Peter, Billy, Charlotte, Sweedal]

own_status = [True, False, False, False, False, False, False, False, False]
owner_name = [None, None, None, None, None, None, None, None, None]


for i in data:
    print(i)

print(data[1]['name'])

eval('Peter').move(rolls1[1])
Peter.position_execution(data, own_status, owner_name)


print(own_status)
print(owner_name)
print(Peter.balance)

Peter.move(9)
Peter.position_execution(data, own_status, owner_name)