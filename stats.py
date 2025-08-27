def get_num_words(book_text):
    return len(book_text.split())

def per_symbol_stats(book_text):
    stats = {}

    for symbol in book_text:
        if symbol != '':
            symbol_lower = symbol.lower()
            if symbol_lower in stats:
                stats[symbol_lower] += 1
            else:
                stats[symbol_lower] = 1

    return stats
