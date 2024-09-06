import random
from collections import Counter

someWords = '''apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
# randomly choose a secret word from our "someWords" LIST.
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    for i in word:
        # For printing the empty spaces for letters of the word
        print('_', end=' ')
    print()

    playing = True
    # list for storing the letters guessed by the player
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0

    while (chances != 0) and flag == 0:  # flag is updated when the word is correctly guessed
        print()
        print('No of chances left:',chances)
        chances -= 1

        guess = input('Enter a letter to guess: ')

        # Validation of the guess
        if not guess.isalpha():
            print('Enter only a LETTER')
            continue
        elif len(guess) > 1:
            print('Enter only a SINGLE letter')
            continue
        elif guess in letterGuessed:
            print('You have already guessed that letter')
            continue

        # If letter is guessed correctly
        if guess in word:
            # k stores the number of times the guessed letter occurs in the word
            k = word.count(guess)
            for i in range(k):
                letterGuessed += guess  # The guessed letter is added as many times as it occurs

        # Print the word
        for char in word:
            if char in letterGuessed:
                print(char, end=' ')
            else:
                print('_', end=' ')
        print()

        # Check if the user has guessed all the letters
        if Counter(letterGuessed) == Counter(word):
            print("The word is: ", end=' ')
            print(word)
            flag = 1
            print('Congratulations, You won!')
            break

    # If user has used all of his chances
    if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
        print()
        print('You lost! Try again..')
        print('The word was ',word)











