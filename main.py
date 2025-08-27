from stats import get_num_words, per_symbol_stats

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("./books/frankenstein.txt")

    symbol_stats = per_symbol_stats(book_text)

    for symbol, count in symbol_stats.items():
        print("'" + str(symbol) + "'" + ": " + str(count))

main()
