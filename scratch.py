def sweap_max(items: list) -> list:
    max_pos = items.index(max(items))
    items[0], items[max_pos] = items[max_pos],items[0]
    return items

a = [10, 21, 19, 9, 22]
result = sweap_max(a)
print(result)