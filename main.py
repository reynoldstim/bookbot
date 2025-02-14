path_to_file = "books/frankenstein.txt"


def main():
    with open(path_to_file) as f:
        file_content = f.read()
        word_count = count_words(file_content)
        char_count = count_characters(file_content)
        char_count = formatted_char_count(char_count)

        print_report(path_to_file, word_count, char_count)


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    lower = text.lower()
    char_dict = {}
    for letter in lower:
        if letter not in char_dict:
            char_dict[letter] = 1
        else:
            char_dict[letter] = char_dict[letter] + 1
    return char_dict


def formatted_char_count(char_count):
    list_dicts = []
    for char in char_count:
        if char.isalpha():
            list_dicts.append({"char": char, "count": char_count[char]})
    list_dicts.sort(reverse=True, key=lambda x: x["count"])
    return list_dicts


def print_report(book, word_count, char_count_list):
    print(f"--- Begin report of {book} ---")
    print(f"Word count: {word_count}")

    for entry in char_count_list:
        print(f"The '{entry["char"]}' character was found {entry["count"]} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
