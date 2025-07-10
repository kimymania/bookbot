import sys

from stats import count_characters, count_words, sort_dict


def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        contents = f.read()
    return contents


def main():
    if len(sys.argv) != 2:
        print(len(sys.argv))
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    book = get_book_text(filepath)
    num_words = count_words(book)

    num_chars = count_characters(book)
    chars = sort_dict(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in chars:
        if not char["char"].isalpha():
            continue
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
