# Minigames
This is my first project called Minigames, which includes multiple minigames done in Python.
## Description
This project includes Wordle, Tic Tac Toe. I have finished Wordle, and I am working on Tic Tac Toe game.All games are asingle player game. 
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
