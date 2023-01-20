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

own_status = [False] * 9
own_status[0] = True        # GO Space is not buyable
owner_name = [None] * 9


for i in data:
    print(i)

print(data[1]['name'])

counter = 0
for i in range(len(rolls1)):
    player_turn = p_list[counter]

    player_turn.move(rolls1[i])
    player_turn.position_execution(data, own_status, owner_name, locals())
    counter += 1
    if counter == 4:
        counter = 0
    
    if player_turn.status == True:
        break

p_list.remove(player_turn)

max_val = 0
max_player = None
for i in range(len(p_list)):
    m = p_list[i].balance
    if m > max_val:
        max_val = m
        max_player = p_list[i]

print(f"Winner of notmonopoly is {max_player.name}, with a score of {max_val}")
