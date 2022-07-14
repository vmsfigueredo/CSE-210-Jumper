import random
class Validation:
    #   Validate user input according to List
    def inList(self, message, accepted):
        string = input(message)
        while string.upper() not in accepted:
            valid = "/".join(accepted)
            string = input(f"Please enter a valid value [{valid}]: ")
        return string
    #   Check if user input is a number
    def isNumber(self, message):
        try:
            string = round(float(input(message)), 2)
            return string
        except:
            return round(self.isNumber(), 2)
        
class Player:
    def __init__(self):
        #   Define the Player
        self._player = """
    _______
   /       \\
    -------
    \\     /
     \\   /
       o
     / | \\
      / \\
"""
    #   Draw the player according to its lives
    def draw(self, lives):
        #   Draw the parachute
        parachute = self._player.split('\n')[1:6]
        parachute = parachute[5-lives:]
        print("\n".join(parachute))
        #   Draw the player
        player = "\n".join(self._player.split('\n')[6:])
        if lives == 0:
            player = player.replace("o", "x")
        print(player)

class Guess:
    def __init__(self, difficulty):
        self.difficulty  = difficulty
        #   Words to guess
        #   E = Easy, M = Medium, H = Hard
        self._words = {
            "E": ["Cup", "Life", "Love", "Ride", "Gold", "Wall", "Luck", "More", "Sure", "Pies"],
            "M": ["Piano", "Closet", "Closed", "Weird", "Lucky", "Short", "Control", "Boring"],
            "H": ["Expect", "Although", "Behold", "Scissors", "Enormity", "Eternity", "Literally", "Nitrogen"]
            }
        #   Get a random word according to difficulty
        self.word = random.choice(self._words[difficulty.upper()]).upper()
        #   Define tries and correct guesses
        self.tries = []
        self.correct = []
    #   New Play
    def play(self, guess):
        #   check if user's guess is not duplicated
        if (guess not in self.correct) and (guess not in self.tries):
            #   Define correct as false
            correct = False
            #   Get all the letters in chosen word
            for letter in list(self.word):
                #   Check if letter is equal to user's guess
                if(letter == guess.upper()):
                    #   Set correct to true if letter is equal to user's guess
                    correct = True
            #   Append guess to correct list
            if correct:
                self.correct.append(guess.upper())
            else:
                self.tries.append(guess.upper())
        else:
            #   Return true if guess is duplicated (because user will not lose lives)
            correct = True
        #   Return True or False according to User's guess
        return correct
    
    def createTable(self):
        #   Creating a new Table
        table = []
        #   Getting all letters in chosen word
        for letter in list(self.word):
            #   Checking if letter is already in self.correct list
            if(letter in self.correct):
                #   Append letter to table
                table.append(letter)
            else:
                #   Append _ to table (hidden letter)
                table.append("_")
        return table
    
    #   Draw the guessing word
    def draw(self):
        #   Creating a new Table
        table = self.createTable()
        #   Draw the table
        print(" ".join(table))
    
    #   Check if user won the game
    def check(self):
        #   Creating a new Table
        table = self.createTable()
        #   Checking if table lenght is greater then 0 and if "_" not exists in table
        if len(table) > 0 and "_" not in table:
            return True
        return False
            
class Game:
    
    def __init__(self):
        self.playing = 1
        self.lives = 5
        
    #   Game's main Function
    def start(self, difficulty):
        #   Init Validation Class
        inputValidation = Validation()
        
        #   Init Guess Class
        guess = Guess(difficulty)
        
        #   Init Player Class
        player = Player()
        
        #   Game Looping
        while self.playing == 1:
            #   Check if player has lives
            if self.lives > 0:
                #   Draw the player with/without parachute (according to its lives)
                player.draw(self.lives)
                #   Get user's guessing
                letter = inputValidation.inList("Guess a letter [a-z]: ", list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")).upper()
                
                #   Check if user already guessed the letter
                guessed = guess.correct + guess.tries
                while letter in guessed:
                    print("Already guessed letters: " + ", ".join(guessed))
                    letter = inputValidation.inList("You already tried to guess this letter, Guess another letter [A-Z]:", list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")).upper()
                #   Play
                if guess.play(letter) == False:
                    #   Removes 1 life point if user got the wrong guessing
                    self.lives = self.lives - 1
                #   Update Guessed List
                guessed = guess.correct + guess.tries
                #   Sort Guessed List Alphabetically
                guessed.sort()
                #   Draw the table
                guess.draw()
                print("\n")
                print("Already guessed letters: " + ", ".join(guessed))
                
                #   Check if user won the game
                if guess.check():
                    self.playing = 0
                    print("\nCongrats! You guessed the word!")
            else:
                #   Game over message
                print(f"Game Over, you lose!\nThe word was: {guess.word}")
                self.playing = 0
            
            
    def menu(self):
        #   Game menu
        print("Welcome to Jumper Game!")
        inputValidation = Validation()
        #   Select difficulty
        dif = inputValidation.inList("Please enter the difficulty E for Easy, M for Medium or H for Hard: ", ["E", "M", 'H'])
        self.start(dif)
        return False
    
#   Init Game Class
game = Game()

#   Main Function
def main():
    while game.menu() != False:
        game.menu()
        
#   Init program
if __name__ == '__main__':
    main()