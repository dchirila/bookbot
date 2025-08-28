import sys
from stats import get_num_words, per_symbol_stats, get_sorted_list_of_dicts, expand_stats

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:  # correct number of arguments
        book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)

    symbol_stats = get_sorted_list_of_dicts(
        per_symbol_stats(book_text)
    )

    report = f"""
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
    """

    for symbol_dict in symbol_stats:
        report += f"{symbol_dict['char']}: {symbol_dict['num']}\n"

    report += "============= END ===============\n"
    
    print(report)

main()
