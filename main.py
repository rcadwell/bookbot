import sys
from stats import get_num_words, get_chars_dict, sort_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    word_count = get_num_words(text)
    print(f'Found {word_count} total words')

    raw_char_counts = get_chars_dict(text)
    sorted_char_data = sort_char_counts(raw_char_counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_char_data:
        character = item["char"]
        count = item["num"]
        print(f"{character}: {count}")

    print("============= END ===============")

main()