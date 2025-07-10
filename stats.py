def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def sort_dict(dictionary):
    new_list = []
    for k, v in dictionary.items():
        item = {
            "char": k,
            "num": v,
        }
        new_list.append(item)
    new_list.sort(reverse=True, key=lambda x: x["num"])
    return new_list
