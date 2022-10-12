The goal of this project was to create a program that could guess complete any Wordle
in as few guesses as possible. If you're not familiar, Wordle is a game where you
try to guess a five letter in six guesses or less. For each guess, you get information
about the answer through your input. To learn more about how the game works, check out
this website: https://www.nytimes.com/games/wordle/index.html

Included in this project is a file called 'word_test.java', which was my method of 
designing my Wordle algorithm. Also included is 'words.txt', a list of the 5757 most common
five letter words. 'word_test.java' takes this list, and analyzes it for letter
frequency, and words that match specific requirements. I used this analysis to determine
what my initial guesses would be in my Wordle program.

The Wordle program works by eliminating possible words from the word list after each 
guess, until the program guesses the correct word. In designing this program, I made
the decision to use two initial guesses. This means that the first two guesses made
by the program are hard-coded for the sole purpose of finding which letters are in
the answer. The downside to this method is that three guess wins are very rare. The 
upside of this method is that the algorithm is extrordinarily reliable. In my testing,
which has included over one hundred unique words, I have yet to see the algorithm fail
to guess the word in six attempts or less.

As a note on the accuracy of this code: I first wrote this program for a coding competition
in one of my second year University classes. The competition involved each competitor 
putting the same 10 random Wordle puzzles through their Wordle code, and the code that
needed the least total guesses to find all 10 words would win. This program won me that
competition.
