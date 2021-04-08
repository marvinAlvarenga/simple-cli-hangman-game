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
    # Use a dictionaty to store each letter from the word with a flag
    # The flag says if the letter has to be hidden or not
    hidden_letters = {letter: True for letter in word}

    while not is_game_over(hidden_letters):
        os.system('clear')
        display_hidden_word(word, hidden_letters)

        attempt = input('Type a letter and then press ENTER: ').lower()
        hidden_letters = update_hidden_letters(attempt, hidden_letters)

    os.system('clear')
    print(f'Congratulations! You guessed the word: {word}')


def is_game_over(letters):
    # If There are no hidden letter, the game is over
    return True not in letters.values()


def display_hidden_word(word, hidden_letters):
    letters_to_show = map(lambda letter: '_' if hidden_letters[letter] else letter, word)

    print('Guess the word!', ' '.join(letters_to_show), sep='\n')


def update_hidden_letters(attempt, letters):
    updated_letters = letters
    if letters.get(attempt):
        updated_letters[attempt] = False

    return updated_letters


if __name__ == '__main__':
    run()
