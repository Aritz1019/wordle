import string

def resolve_wordle(result, initial_word, word_list):

    contained_letters = set()
    letters = list(string.ascii_uppercase)
    letters_map = {}
        
    letters_map = {letter : list(range(1,6)) for letter in letters}

    selected_word = initial_word
    end = False

    while not end:
        print(selected_word)

        compare_words(result, selected_word, letters_map, contained_letters)

        if selected_word == result:
            end = True
        else:
            word_list.remove(selected_word)
            selected_word = select_new_word(word_list, letters_map, contained_letters)
    

def compare_words(result, initial_word, letters_map, contained_letters):

    letter_seen = False

    for i in range(5):
        if initial_word[i] == result[i]:
            letters_map[initial_word[i]] = [i+1]
            contained_letters.add(initial_word[i])

    for i in range(5):
        letter_seen = False
        for result_letter in result:
            if initial_word[i] == result_letter:
                letter_seen = True
                dict_value = letters_map.get(initial_word[i])
                contained_letters.add(initial_word[i])
                if(len(dict_value) > 1):
                    dict_value.remove(i+1)
                break
        if letter_seen == False:
            letters_map[initial_word[i]] = []

def select_new_word(word_list, letters_map, contained_letters):

    filter_word_list(word_list, letters_map, contained_letters)
    
    return word_list[0]

def filter_word_list(word_list, letters_map, contained_letters):

    for word in word_list[:]:
        for i in range(5):
            dict_value = letters_map.get(word[i])
            if dict_value != None:
                if not i+1 in dict_value or not has_letters(word, contained_letters):
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

    resolve_wordle("MACHO","ROBAS", word_list)

if __name__ == "__main__":
    main()