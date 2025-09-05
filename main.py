import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
from stats import wordcount
from stats import charcount
from stats import listionary

def main():
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = wordcount(book_text)
    chars = charcount(book_text)
    sorted_chars = listionary(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_chars:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()