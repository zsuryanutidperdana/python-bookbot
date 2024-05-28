def main():
    path_to_file = "./books/frankenstein.txt"
    file_contents = get_file_text(path_to_file)
    word_count = count_words(file_contents)
    letter_count = get_letter_count(file_contents)
    print('======= WELCOME TO BOOK BOT =======')
    print(f'--- Begin report of {path_to_file[2:]} ---')
    print(f'{word_count} words found in the document')
    print_sorted_char_report(letter_count)
    print('===================================')

def get_file_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    word_list = text.split()
    return len(word_list)

def get_letter_count(text):
    letter_map = {}
    for char in text:
        lowered = char.lower()
        if lowered not in letter_map:
            letter_map[lowered] = 0
        letter_map[lowered] += 1
    return letter_map

def print_sorted_char_report(char_dict):
    list_of_alphabets = []
    for alphabet in char_dict:
        if alphabet.isalpha():
            alphabet_count = {}
            alphabet_count["char"] = alphabet
            alphabet_count["count"] = char_dict[alphabet]
            list_of_alphabets.append(alphabet_count)
    
    list_of_alphabets.sort(reverse=True, key=lambda x:x["count"])
    for e in list_of_alphabets:
        print(f"The '{e["char"]}' character was found {e["count"]} times")
    
    

main()