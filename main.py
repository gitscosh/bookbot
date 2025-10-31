from stats import get_num_words

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
    
def main():
    text = get_book_text('books/frankenstein.txt')
    get_num_words(text)

main()
