import random
import os


def run():
    pull = get_words_pull()
    word = select_word(pull)
    run_game(word)


def get_words_pull():
    with open('./data.txt', 'r', encoding='utf-8') as f:
        words = [word for word in f]

    return words


def select_word(words):
    word = random.choice(words)
    return normalize_word(word)


def normalize_word(word):
    normalized_word = word.lower()
    normalized_word = normalized_word.strip()
    normalized_word = normalized_word.replace('á', 'a')
    normalized_word = normalized_word.replace('é', 'e')
    normalized_word = normalized_word.replace('í', 'i')
    normalized_word = normalized_word.replace('ó', 'o')
    normalized_word = normalized_word.replace('ú', 'u')

    return normalized_word


def run_game(word):
    os.system('clear')
    try:
        live = int(input('How many attempts would you like to try: '))
        if live < 1:
            raise ValueError
    except ValueError:
        os.system('clear')
        print('Sorry \U0001F600. It has to be a number more or equal than 1 ')
        return None

    # Use a dictionaty to store each letter from the word with a flag
    # The flag says if the letter has to be hidden or not
    hidden_letters = {letter: True for letter in word}
    wrong_letters = []

    while not is_game_over(hidden_letters, live):
        os.system('clear')
        display_hidden_word(word, hidden_letters, live, wrong_letters)

        attempt = input('Type a letter and then press ENTER: ').lower()
        if guessed_letter(attempt, hidden_letters):
            hidden_letters = update_hidden_letters(attempt, hidden_letters)
        else:
            wrong_letters.append(attempt)
            live -= 1

    winner = is_winner(live)
    os.system('clear')
    message = (f'Congratulations! You guessed the word: {word}'
               if winner
               else f'Sorry! You failed. The word was: {word}')
    print(message)


def is_game_over(letters, live):
    # If There are no hidden letter, the game is over
    return True not in letters.values() or live == 0


def display_hidden_word(word, hidden_letters, live, wrong_letters):
    letters_to_show = map(lambda letter: '_' if hidden_letters[letter] else letter, word)

    print('Guess the word!',
          '\u2764\ufe0f  ' * live,
          ' '.join(letters_to_show),
          '\n\nWrong letters used: ' + ' '.join(wrong_letters),
          sep='\n')


def guessed_letter(attempt, letters):
    return True if letters.get(attempt) else False


def update_hidden_letters(attempt, letters):
    updated_letters = letters
    updated_letters[attempt] = False
    return updated_letters


def is_winner(live):
    return live != 0


if __name__ == '__main__':
    run()
