def find_word_count(file):
    words = file.split()
    return len(words)

def count_characters(letters: str) -> dict[str, int]:
    counts: dict = {}
    for letter in letters:
        lowercase_letter = letter.lower()
        if lowercase_letter in counts:
            counts[lowercase_letter] += 1
        else:
            counts[lowercase_letter] = 1
    return counts    

def sort_on(key):
    return key[1]

def chars_dict_to_sorted_list(chars_dict: dict[str, int]) -> list:
    sorted_list: list = []
    for char in chars_dict:
        chars_dict[char]
        sorted_list.append((char, chars_dict[char]))
        sorted_chars = sorted(sorted_list, key=sort_on, reverse=True)
    return sorted_chars