import random
arr = []
for i in range(1, 101):
    arr.append(i)
# print(arr)
# print(random.choice(arr))

def easy_mode():
    counter_easy = 10
    random_num_easy = random.choice(arr)
    # print(f'Random number easy mode: {random_num_easy}')
    guess_easy = int(input('Guess the number from 1 to 100: \n'))
    # print(guess_easy, random_num_easy)

    while guess_easy != random_num_easy:
        if guess_easy < random_num_easy:
            print('Guess a higher number')
        else:
            print('Guess a lower number')

        guess_easy = int(input('Try Again. Guess the number from 1 to 100: \n'))
        counter_easy -= 1
        if counter_easy == 0:
            return print(f'Out of guesses\nThe correct number is {random_num_easy}')
        print(counter_easy)

        if guess_easy == random_num_easy:
            return print(f'Correct Guess: {guess_easy}')

def hard_mode():
    counter_hard = 5
    random_num_hard = random.choice(arr)
    # print(f'Random number easy mode: {random_num_easy}')
    guess_hard = int(input('Guess the number from 1 to 100: \n'))
    # print(guess_easy, random_num_easy)

    while guess_hard != random_num_hard:
        if guess_hard < random_num_hard:
            print('Guess a higher number')
        else:
            print('Guess a lower number')

        guess_hard = int(input('Try Again. Guess the number from 1 to 100: \n'))
        counter_hard -= 1
        if counter_hard == 0:
            return print(f'Out of guesses:\nThe correct number is {random_num_hard} ')
        print(counter_hard)

        if guess_hard == random_num_hard:
            return print(f'Correct Guess: {guess_hard}')

easy_or_hard = input("Type 'e' for easy\nType 'h' for hard\n")
if easy_or_hard == 'e':
    easy_mode()
elif easy_or_hard == 'h':
    hard_mode()