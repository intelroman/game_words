#!/usr/bin/python3
import time, random, re, sys, signal, json, os

def catc_ctrl_c(sig,frame):
    print ("Ctrl-c is disabled")
signal.signal(signal.SIGINT, catc_ctrl_c)

games = []
def pywalker(path):
    for root, dirs, files in os.walk(path):
        for file_ in files:
            games.append(os.path.join(root, file_))
pywalker('words')

def select_game():
    a = 0
    while True:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print ("Select game from the list:")
        print ("Total games are: {}".format(len(games)))
        for i,j in enumerate(games):
            print ("{}) {} and contain {} words".format (i+1,j,len(open(j).read().splitlines())))
        print ("Type quit or q to exit the game")
        if a == 0:
            last = ' '
        print ("{}".format(last))
        key_in = input('Select form 1 to '+ str(len(games))+':').lower()
        try:
            if str(key_in) == 'quit' or str(key_in) == 'q':
                sys.exit("Game quited , Bye Bye")
            val = int(key_in)
            if val <= len(games) and val > 0:
                val = (val - 1)
                return games[val]
            elif val <= 0:
                last = 'Selected number is less than 1'
                a += 1
            else:
                last = ("Selected number is bigger than "+str(len(games)))
                a += 1
        except ValueError:
            last = "That's not an int! No.. input string is not an Integer. It's a string"
            a += 1

for i,j in enumerate(games):
    print ("{}) {}".format (i+1,j))

def main_var():
    words = open(select_game()).read().splitlines()
    word = random.choice(words).lower()
    list_word = []
    for i in word:
        list_word.append(i)
    lives = len(list_word)
    letters = []
    return words, word, list_word, lives, letters;

def letter_input():
    while True:
        str_input = input("Enter a letter:").lower()
        if "quit" in str_input:
            sys.exit("Game quited , Bye Bye")
        if not re.match("^[a-z]{1}$", str_input):
            print ("You are only allowed to use letter, no numbers and no more that 1 character\nOr type quit to exit the game")
        else:
            return str_input

def disp_word(letters,word,list_word):
    if len(letters) == 0:
        print("-"*len(word))
    else:
        tmp_word = []
        for j,i in enumerate(list_word):
            if i in "".join(letters):
                tmp_word.append(i)
            else:
                tmp_word.append("-")
        print ("".join(tmp_word))

def end():
    while True:
        question_end = input("Restart yes or no ").lower()
        if "yes" == question_end or question_end == "y":
            print("Starting new game...")
            main()
        elif "no" == question_end or question_end == "n":
            sys.exit("Game quited , Bye Bye")
        else:
            print("Please chose yes/no or y/n")

def main():
    words, word, list_word, lives, letters = main_var()
    while lives != 0 :
        if len(letters) == len(set(list_word)):
            print ("You win")
            end()
        letter = ''
        print ("Lives remain: {}".format (lives))

        disp_word(letters,word,list_word)
        letter = letter_input()
        for i in letters:
            if letter in letters:
                print ("You already use letter \"{}\", please use other letter".format(letter))
                letter = letter_input()

        if letter in word:
            print ("You guess a letter")
            letters.append(letter)
        else:
            lives -= 1
    end()

if __name__ == "__main__":
    main()
