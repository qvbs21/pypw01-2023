from string import punctuation


def words_count(text: str) -> dict:
    dictionary = {}
    text = text.lower()
    for char in punctuation:
        text = text.replace(char, "")

    for word in text.split():
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary


result = words_count("Many many. super views in this world")
print(result)
