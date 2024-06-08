def get_text(path_to_file: str = "books/frankenstein.txt") -> tuple[str, str]:
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents, path_to_file


def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)


def get_freq_chr(text: str) -> dict:
    text_list = [i for i in set(text.lower()) if i.isalpha()]
    text_list.sort()
    return {i: text.lower().count(i) for i in text_list}


def boot_dev_report():
    text, bookpath = get_text()
    nr_words = get_word_count(text)
    letters_freq = get_freq_chr(text)
    print()
    print(f"--- Begin report of {bookpath} ---")
    print(f"{nr_words} words found in document")
    print()
    for letter in sorted(letters_freq, key=letters_freq.get, reverse=True):
        print(f"The '{letter}' character was found {
              letters_freq[letter]} times")

    print("--- End report ---")


def main():
    boot_dev_report()


if __name__ == "__main__":
    main()
