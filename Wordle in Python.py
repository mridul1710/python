#name: Mridul KC
#grace days used: 0

from operator import iand
import sys
import termcolor
import random

class Wordle:  #setting up the class
    #remove pass and start writing your code
    currentWord = ""
    numberOfUserGuesses = 0

    def __init__(self, guesses, file):  #setting up the object
        self.guesses = guesses   #initialization
        self.file = file

    def readFile(self):
        handle = open(self.file,'r') #open the passed file
        self.wordList = []  #all the words from the text file go into the empty list

        check = "check"
        while check != "":            #checking for end of file
            check = handle.read(6)    #retrieving 5 characters and new line character
            if check != "":            #checking for empty string
                self.wordList.append(check)  #adding words from file to the instance variable wordList

        handle.close() #this code serves to close the file handler handle

    def selectRandomWord(self):

        self.currentWord = random.choice(self.wordList)   #pick a random word from the passed file and assign it to currentWord

    def removeNewLineFromWord(self):
        self.currentWord = self.currentWord.rstrip("\n")  #removing white spaces
        print(self.currentWord)
        print(len(self.currentWord))

    def playWordle(self): #function for the actual game

        while self.numberOfUserGuesses < self.guesses: #controls the number of attempts user has
            self.numberOfUserGuesses += 1
            guess = input("\n Guess Number {}:".format(self.numberOfUserGuesses)) #taking user's guess


            for i in range(5): #checks every letter of the word that the user entered
                if guess[i] == self.currentWord[i]: #compares the letters of the input word and current word

                    print(termcolor.colored(guess[i], 'green'), end="")  #displays appropriate color according to the letters position
                elif guess[i] in self.currentWord:
                    print(termcolor.colored(guess[i], 'yellow'), end="")  #displays appropriate color according to the letters position
                else:
                    print(guess[i], end="")

            if guess == self.currentWord:  #text to display if user manages to guess the right word
                print("\n Congrats on getting today's wordle which was {}! You got it in {} tries".format(guess,self.numberOfUserGuesses))
                self.numberOfUserGuesses = self.guesses + 1 #to avoid while loop (parent loop) because the user already wont the game

            elif self.numberOfUserGuesses == self.guesses: #text to display if user does not guess the word
                print("\n You were not able to guess {} in {} tries. Try again!".format(self.currentWord,self.numberOfUserGuesses))

        
        exit()

            

        






















                






#Code that instantiates your wordle class and runs it
game = Wordle(6, "myWords.txt")
game.readFile()
game.selectRandomWord()
game.removeNewLineFromWord()
game.playWordle()
