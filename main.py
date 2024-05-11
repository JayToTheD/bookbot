def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    word_count = get_word_count(text)
    letter_counts = get_letter_counts(text)
    letters_sorted = get_sorted_letters(letter_counts)
    print(f"---Begin report of {file_path}---")
    print(f"{word_count} words found in the document")
    print("")
    for entry in letters_sorted:
        print(f"The {entry["letter"]} character was found {entry["num"]} times")
    print("---End of report---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_counts(text):
    text_lowercase = text.lower()
    letters = {}
    for letter in text_lowercase:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1 
    return letters

def sort_on(dictionary):
    return dictionary["num"]

def get_sorted_letters(dictionary):
    letters_sorted = []
    empty_dictionary = {}
    letters = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        ]
    for entry in dictionary:
        if entry in letters:
            empty_dictionary["letter"] = entry
            empty_dictionary["num"] = dictionary[entry]
            letters_sorted.append(empty_dictionary)
            empty_dictionary = {}
    letters_sorted.sort(reverse=True, key=sort_on)
    return letters_sorted


main()
