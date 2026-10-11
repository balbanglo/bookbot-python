#!/usr/bin/python3

# This is an project for Boot.dev.

import sys 

from stats_for_bookbot import find_word_count
from stats_for_bookbot import count_characters
from stats_for_bookbot import chars_dict_to_sorted_list


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, word_count, sorted_list_of_char_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)
    total_words = find_word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list_of_char_counts:
        if not item[0].isalpha():
            continue
        letter = item[0]
        count = item[1]
        print(f"{letter}: {count}")
    print("============= END ===============")    




def main():
    if len(sys.argv) < 2:
        print("ERROR: No e-book path, please insert a ebook path to it to read it.\nCommand: python3 bookbot.py <path_to_ebook>\nOR\nCommand (make sure you have a shebang (#!/usr/bin/python3) to tell the shell to use python3): ./bookbot.py <path_to_ebook>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = find_word_count(book_text)
    character_counts = count_characters(book_text)
    sorted_char_list = chars_dict_to_sorted_list(character_counts)
    print_report(book_path, word_count, sorted_char_list)

main()   
