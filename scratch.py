def sweap_max(items: list) -> list:
    max_pos = 0
    for i in range(len(items)):
        if items[i] >= items[max_pos]:
            max_pos = i
    temp = items[0]
    items[0] = items[max_pos]
    items[max_pos] = temp
    return items

a = [10, 21, 19, 9, 4]
result = sweap_max(a)
print(result)