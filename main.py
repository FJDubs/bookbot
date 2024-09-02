def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    print(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()