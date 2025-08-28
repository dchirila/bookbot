def get_num_words(book_text):
    return len(book_text.split())

def per_symbol_stats(book_text):
    stats = {}
    book_text_lower = book_text.lower()

    for symbol in book_text:
        if (symbol == '\ufeff') or (symbol == '\n'):
            continue
        else:
            symbol = symbol.lower()
            if symbol in stats:
                stats[symbol] += 1
            else:
                stats[symbol] = 1

    return stats

def expand_stats(stats):
    stats_expanded_list_of_dicts = []
    for key, value in stats.items():
        stats_expanded_list_of_dicts.append({"char": key, "num": value})
    return stats_expanded_list_of_dicts

def get_sorted_list_of_dicts(stats):
    stats_expanded_list_of_dicts = expand_stats(stats)

    stats_expanded_list_of_dicts.sort(
        key=lambda x: x['num'],
        reverse=True
    )

    return stats_expanded_list_of_dicts
