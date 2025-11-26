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
    return chars;

def sort_on(item_dict):
    return item_dict["num"] # This tells .sort() to look at the 'num' value


def sort_char_counts(chars_dict):
    list_of_chars = []
    for character, count in chars_dict.items():
        if not character.isalpha():
            continue
        
        new_dict = {"char": character, "num": count}
        list_of_chars.append(new_dict)
     
    list_of_chars.sort(reverse=True, key=sort_on)

    return list_of_chars
    