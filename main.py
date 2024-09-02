def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    word_count = get_word_count(text)
    char_counts = char_count(text)
    print(char_counts)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_counts = {}
    for t in text.lower():
        if t not in char_counts.keys():
            char_counts[t] = 0
        char_counts[t] += 1
    return char_counts

main()