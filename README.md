Woven Monopoly

The code is written in Python 3.9.7
### How it works
Deterministic dice rolls are provided in addition to the game board. The dice roll files are included in the test.py file where there are 12 tests. The file can be run like any normal python files. The tests are not all inclusive and include a bit of repetition. Additionally, the two rolls are included in the wovenmonopoly.py file where it is possible to comment out each game. However, do not comment out both as global variables are shared here.


### Design decisions
The game is pretty straight forward. I created a player class in playerdef containing the relevant information to keep track of. A player moves a certain amount of positions and then the positions effect is executed. The GO tile wrap around is handled with modulus and adding additional currency to the player. 
The properties are handled a bit differently, I was thinking about making properties a class by itself and then expanding the current player class with a field to see each players owned properties. However, as Woven Monopoly is a pretty simple game with a board that does not change state, I think it was easier to add a couple of arrays keeping track of owned status and its owner. Because of this, I did not utilise the Colour field in the board.json file as I just kept track of its position. I included a properties.py file to show how a possible extension to the program could look, especially if the tiles on the Monopoly game was randomised.
Bankrupt only happens if balance is negative, not zero.


### Results
Game 1 - 
Peter wins with a score of 40 and ended on Lanzhou Beef Noodle
Billy was on Lanzhou Beef Noodles with 18 coins
Charlotte was on The Burval with 0 coins
Sweedal was on Gami Chicken with -5

Game 2 -
Billy wins with a score of 27 and ended on The Grand Tofu
Peter was on Massizim with 5 coins
Charlotte was on GO with 21 coins
Sweedal was on Massizim with -3 coins