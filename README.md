# Minigames
This is my first project called Minigames, which includes multiple minigames done in Python.
## Description
This project includes Wordle, Tic Tac Toe, and Tower of Hanoi. Each game is played on the terminal.
### Wordle
This is a game that a user guesses the possible 5 letter word answers. 
- If the letter is correctly guessed at the right position, prints 'o'. 
- If the letter is in the answer, but in a different index, the program prints '^'.
- If the letter does not exist in the answer, the program print '?'.
- The answer is choosen from the list of 100 5 letter words, ["apple","korea","hello","today","leggo"].
- The user have 10 chances for guessing the correct word.
- The user can possibly get 100 in the first try.
- Every time the user incorrectly guess the word, chance is getting decreased by 1, and the max score is decreased by 10.
- If the user wants to give up during the game, they can type "stop" to finish the game.
- If the user wants to start the game again, the user enters "yes", If not, total score is printed out.
- We got the list of possible answers from https://github.com/bdholt1/five-letter-words/blob/main/sgb-words.txt
### TicTacToe
This is a two-player game where each user selects their own shape (O or X) and takes turns placing it on the board.
- If the same shape is placed three times in a row — horizontally, vertically, or diagonally — the player using that shape wins the game.
- Once a shape is placed on the board, it cannot be changed or removed.
- If the board becomes full and no player has won, the game ends in a tie.
- If a player enters an invalid index, an error message will be displayed and the player will be asked to enter the index again.
- After each turn, the updated board will be printed in the terminal.
- ### Tower of Hanoi
-
