def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_num(entry):
    return entry["num"]

def sorted_list(letters):
    char_list = [{'char': char, 'num': num} for char, num in letters.items()]
    char_list.sort(reverse=True, key=get_num)
    return char_list

