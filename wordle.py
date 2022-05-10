def resolve_wordle(result, initial_word, word_list):

    final_word = '*****'
    contained_letters = set()
    not_contained_letters = set()
    selected_word = initial_word
    end = False

    while not end:
        print(selected_word)

        final_word = compare_words(result, selected_word, final_word, contained_letters, not_contained_letters)

        if final_word.count('*') == 0:
            end = True
        else:
            word_list.remove(selected_word)
            selected_word = select_new_word(final_word, word_list, contained_letters, not_contained_letters)
    

def compare_words(result, initial_word, final_word, contained_letters, not_contained_letters):

    letter_seen = False

    for i in range(5):
        if initial_word[i] == result[i]:
            final_word = final_word[:i] + initial_word[i] + final_word[i + 1:]
            contained_letters.add(initial_word[i])

    for initial_word_letter in initial_word:
        letter_seen = False
        for final_word_letter in result:
            if initial_word_letter == final_word_letter:
                letter_seen = True
                contained_letters.add(initial_word_letter)
                break
        if letter_seen == False:
            not_contained_letters.add(initial_word_letter)

    return final_word

def select_new_word(final_word, word_list, contained_letters, not_contained_letters):

    filter_word_list(final_word, word_list, contained_letters, not_contained_letters)
    
    return word_list[0]

def filter_word_list(final_word, word_list, contained_letters, not_contained_letters):

    # me falta mirar que las letras esten en una posicion que puedan estar --> para que no se repitan las mismas letras en las mismas posiciones

    for word in word_list[:]:
        if len(contained_letters) != 0 or len(not_contained_letters) != 0:
            if has_letters(word, not_contained_letters):
                word_list.remove(word)
            elif not has_letters(word, contained_letters):
                word_list.remove(word)
            elif final_word != '*****':
                for i in range(5):
                    if final_word[i] != '*':
                        if final_word[i] != word[i]:
                            word_list.remove(word)
                            break

def has_letters(word, letters):
    for letter in letters:
        if not letter in word:
            return False
    return True

def main():
    file_name = 'words.txt'

    with open(file_name, encoding='UTF-8') as f:
        word_list = f.read().split(' ')

    resolve_wordle("SERIO","OSCAR", word_list)

if __name__ == "__main__":
    main()