import random
from random_words import word_list

word = random.choice(word_list)

def play():
    letter_count = len(word)
    guess_limit = 6
    incomplete_word = letter_count * "_"
    letter_list = []
    word_list =[]
    while guess_limit > 0:
        print("\n")
        #print("\n")
        print(fr"This is a your word: " + incomplete_word)
        guess = input("make a guess: ")
        if len(guess) == 1 and guess.isalpha():
            if guess in letter_list:
                print("you already guessed this letter")
                guess_limit -= 1
            elif guess in word:
                print("Correct!")
                letter_list.append(guess)
                guess_limit -= 1
                list_of_indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in list_of_indices:
                    incomplete_word = incomplete_word[:index] + guess + incomplete_word[index + 1:]
                if incomplete_word == word:
                    print("CONGRATULATIONS, YOU WON!!!!")
                    return
                    break
                print("Current Word " + incomplete_word)
            else:
                print("sorry, there is no", guess, "in the word")
                letter_list.append(guess)
                guess_limit -= 1
        elif len(guess) == len(word) and guess.isalpha():
            if guess == word:
                print("CONGRATULATIONS, YOU WON!!!!")
                return
                break
            elif guess in word_list:
                print("you already guessed this word")
                word_list.append(guess)
                guess_limit
        else:
            print("This is an invalid guess")
            guess_limit -= 1
    print("\n You exceeded maximum number of attempts. Program terminates")
    print("The Answer was: " + word)

play()
