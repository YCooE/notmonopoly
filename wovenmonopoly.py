import json

import playerdef as p_init

board_file = open('board.json')
roll_file1 = open('rolls_1.json')
roll_file2 = open('rolls_2.json')

data = json.load(board_file)

rolls1 = json.load(roll_file1)
rolls2 = json.load(roll_file2)

Peter = p_init.Player("Peter", 16, 0, False)
Billy = p_init.Player("Billy", 16, 0, False)
Charlotte = p_init.Player("Charlotte", 16, 0, False)
Sweedal = p_init.Player("Sweedal", 16, 0, False)

p_list = [Peter, Billy, Charlotte, Sweedal]

own_status = [False] * 9
own_status[0] = True        # GO Space is not buyable
owner_name = [None] * 9


#for i in data:
#    print(i)

def game(rolls, own_status, owner_name, scope, p_list):
    counter = 0
    for i in range(len(rolls)):
        player_turn = p_list[counter]
        player_turn.move(rolls[i])
        player_turn.position_execution(data, own_status, owner_name, scope)
        
        counter += 1
        if counter == 4:
            counter = 0
        
        if player_turn.status == True:
            p_list.remove(player_turn)
            break
    
    # Finds max value and max value player
    max_val = 0
    max_player = None
    for j in range(len(p_list)):
        m = p_list[j].balance
        if m > max_val:
            max_val = m
            max_player = p_list[j]

    print(f"Winner of wovenmonopoly is {max_player.name}, with a score of {max_val}")
    return max_player.name, max_val, owner_name, own_status

#### Uncomment for game1
#max_play1, max_val1, own_name1, own_stat1 = game(rolls1, own_status, owner_name, locals(), p_list)
#print(f"{max_play1} was on {data[Peter.position]['name']}")
#print(f"Billy was on {data[Billy.position]['name']} with {Billy.balance} coins")
#print(f"Charlotte was on {data[Charlotte.position]['name']} with {Charlotte.balance} coins")
#print(f"Sweedal was on {data[Sweedal.position]['name']} with {Sweedal.balance} coins")

#### Uncomment for game2
#max_play1, max_val1, own_name1, own_stat1 = game(rolls2, own_status, owner_name, locals(), p_list)
#print(f"{max_play1} was on {data[Billy.position]['name']}")
#print(f"Peter was on {data[Peter.position]['name']} with {Peter.balance} coins")
#print(f"Charlotte was on {data[Charlotte.position]['name']} with {Charlotte.balance} coins")
#print(f"Sweedal was on {data[Sweedal.position]['name']} with {Sweedal.balance} coins")