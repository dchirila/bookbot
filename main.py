def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(book_text):
    return len(book_text.split())

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    print(f"{count_words(book_text)} words found in the document")

main()
