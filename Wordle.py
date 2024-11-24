#if letter input value at the certain index == the random word's value at the same index -> green,o
#elif letter exist but not the right location, yellow ,^
#else gray, ?

# hello
# hlaxy
# o^???

#possoible lise=[hdjd,dddd,dd,ddd,d]
#correct_answer=[a,p,p,l,e]
#take input from user
#go through the string to check each charater's status
#return result by showing the symbol o,^, or ?
#repeat 6_8 until the response match or "GG"

# initializing wordle: starts a new session with user, set score to 0, number of attempts to 0
# replay with same word - not doing this
# restart with new word - yes - ask "Do you want to play a new game?" after game over
    # do not reset score
    # choose new "answer" from list of possible answers
    # reset the number of attempts 
# user has 10 attempts. start with 100 points, after each attempt, the score decreases by 10

import random


class Wordle:
    def __init__(self,possible_answers,score,chances):
        self.possible_answers = possible_answers
        self.chances=chances
        self.score=score
        self.choose_answer()
        print("Welcome to the game. Lets try to guess world!")
        self.totalScore=0
        self.play_game()

    def choose_answer(self):
        #self.answer = random.choice(self.possible_answers)
        self.answer = "apple"

    def play_game(self):
        continued=True
        while(continued and self.chances>0):
            guess=input("Enter the guess ")
            if len(guess)!=5:
                print("Only 5 letter words are acceptable. ")
            else:
                result = ["?", "?", "?", "?", "?"]
                answer_letters = list(self.answer)
                for i in range(0,5):
                    if guess[i].lower()==self.answer[i]:
                        result[i] = "o"
                        answer_letters.remove(guess[i].lower())
                for i in range(0, 5):
                    if guess[i].lower() in answer_letters:
                        result[i] = '^'
                        answer_letters.remove(guess[i].lower())
                print(result)
                if(result==["o", "o", "o", "o", "o"]):
                    continued=False
                    print("You win!")
                    break
            keepGoing=input("enter 'stop' to finish or enter any key to continue ").lower()

            if(keepGoing=="stop"):
                continued=False
                self.score=0

            else:
                self.score-=10
                self.chances-=1
                print(f"You have {self.chances} more chances, and possible score is {self.score}")  

        print(f"Your score is {self.score}")
        self.totalScore+=self.score
        again=input("Do you want to play again? Enter yes or no ").lower()
        if(again=="yes"):
            self.restart_game()
        else:
            print("Your total score is %s" % self.totalScore)

        # check if input is length 5
        # check and return O, ^, ?
        # check if user won/lost
            # ask if user wants to play agaim
            # (re)starts a new game
       
        


    def restart_game(self):
        self.choose_answer()
        self.chances=10
        self.score=100
        self.play_game()

wordle_game = Wordle(["apple","korea","hello","today","leggo"],100,10)