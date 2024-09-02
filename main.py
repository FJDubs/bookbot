def main():
    path_to_file = "books/frankenstein.txt"
    print_report(path_to_file)

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

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    dict_list = []
    for d in dict:
        if d.isalpha():
            dict_list.append({"letter": d, "num": dict[d]})
    dict_list.sort(reverse = True, key=sort_on)
    return dict_list


def print_report(path):
    text = get_book_text(path)
    wc = get_word_count(text)
    cc = sort_dict(char_count(text))
    print(f"--- Begin report of {path} ---")
    print(f"{wc} words found in the document")
    print()
    for c in cc:
        print(f"The '{c["letter"]}' character was found {c["num"]} times")
    print("--- End Report ---")

main()