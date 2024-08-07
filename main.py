def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_characters(text)
    chars_sorted_list = sort_on(chars_dict)

print(f"--- Begin report of {book_path} ---")
print(f"{num_worlds} words found in the document")
print()

for item in chars_sorted_list:
    if not item["char"].isalpha():
        continue
    print(f"The '{item['char']}' character was found '{item['num']}' times")

print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def sorted(dict):
    return dict["num"]

def sort_on(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append[{"char": ch, "num": num_chars_dict[ch]}]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_characters(text):
    lower_case = text.lower()
    text_dict = {}
    for i in lower_case:
        if i in text_dict:
            text_dict[i] += 1
        else:
            text_dict[i] = 1

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()