def ryerson_letter_grade(pct): 
    
    if pct>=0 and pct<=49:
        return('F')
    elif pct>=50 and pct<=52:
        return('D-')
    elif(pct>=53 and pct<=56):
        return('D')
    elif(pct>=57 and pct<=59):
        return('D+')
    elif(pct>=60 and pct<=62):
        return('C-')
    elif(pct>=63 and pct<=66):
        return('C')
    elif(pct>=67 and pct<=69):
        return('C+')
    elif(pct>=70 and pct<=72):
        return('B-')
    elif(pct>=73 and pct<=76):
        return('B')
    elif(pct>=77 and pct<=79):
        return('B+')
    elif(pct>=80 and pct<=84):
        return('A-')
    elif(pct>=85 and pct<=89):
        return('A')
    elif(pct>=90 and pct<=150):
        return('A+')
    elif(pct>150):
        return('not in range')
    #Edit by BrownMamba*


def is_ascending(items):
    last_item = None

    for item in items:
        if last_item and last_item >= item:
            return False

        last_item = item

    return True


def double_until_all_digits(n, giveup=1000):
    for i in range(giveup):
        if set(list('0123456789')).issubset(list(str(n))):
            return i

        n *= 2

    return -1


# def caps_lock_stuck(text):
#     """
#     TODO Should work but doesn't pass
#     """
#     caps_lock = False
#     new_text = ''
#
#     for char in text:
#         if char.lower() in ['a', 'z']:
#             caps_lock = not caps_lock
#             continue
#
#         new_text += char.swapcase() if caps_lock else char
#
#     return new_text


def scrabble_value(word, multipliers):
    __scrabble__ = {
        "a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4,
        "i": 1, "j": 8, "k": 5, "l": 1, "m": 3, "n": 1, "o": 1, "p": 3,
        "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
        "y": 4, "z": 10
    }

    score = 0

    for i, char in enumerate(word):
        if char not in __scrabble__:
            return

        score += __scrabble__[char] * multipliers[i]

    return score


def create_zigzag(rows, cols, start=1):
    grid = []

    for row in range(rows):
        begin = start + row * cols
        end = begin + cols
        r = list(range(begin, end))

        grid.append(r if row % 2 == 0 else r[::-1])

    return grid


# def contains_bingo(card, numbers, centerfree=True):
#     """
#     TODO Test fails for some reason
#     """
#     rows = []
#     size = 5  # Should be => size % 2 == 1
#
#     # Horizontal & Vertical
#     for x in range(size):
#         h_row = []
#         v_row = []
#
#         for y in range(size):
#             if x == y == ((size - 1) / 2) and centerfree:
#                 continue
#
#             h_row.append(card[x][y])
#             v_row.append(card[y][x])
#
#         rows.append(h_row)
#         rows.append(v_row)
#
#     # Diagonals
#     d_rows = [
#         [card[size - i - 1][i] for i in range(size)],
#         [card[i][i] for i in range(size)]
#     ]
#
#     for row in d_rows:
#         if centerfree:
#             del row[(size - 1) / 2]
#
#     rows += d_rows
#
#     for row in rows:
#         if set(row).issubset(numbers):
#             return True
#
#     return False


def group_equal(items):
    groups, group = [], []

    for i, item in enumerate(items):
        group.append(item)

        if i + 1 >= len(items):
            groups.append(group)
            continue

        next_item = items[i + 1]

        if next_item == item:
            continue

        groups.append(group)
        group = []

    return groups


# def recaman(n):
#     """
#     TODO
#     """
#     pass
#
#
# def running_median_of_three(items):
#     """
#     TODO
#     """
#     pass


def detab(text, n=8, sub=' '):
    while True:
        tab_index = text.find('\t')

        if tab_index == -1:
            break

        text = text.replace('\t', (n - n % tab_index) * sub, 1)

    return text


def reverse_ascending_sublists(items):
    """
    Refactor maybe?
    """
    cur = 0

    for i, item in enumerate(items):
        if i + 1 >= len(items) or item >= items[i + 1]:
            items[cur:i + 1] = items[cur:i + 1][::-1]
            cur = i + 1

    return items


def hand_is_badugi(hand):
    all_items = [item for card in hand for item in card]

    return len(set(all_items)) == len(all_items)


def brangelina(first, second):
    """
    TODO
    """
    import re

    first_groups = re.split('[aeiou]+', first)
    second_groups = re.split('[aeiou]+', second)

    return first_groups, second_groups


def sort_by_digit_count(items):
    collection = []

    for item in items:
        nums = ''.join([str(c) for c in set(str(item))])
        collection.append(nums)

    print(sorted(collection))
#    return collection

if __name__ == '__main__':
    print(sort_by_digit_count([98, 19, 4321, 9999, 73, 241, 111111, 563, 33]))
    print(sort_by_digit_count([1234, 4321, 3214, 1243]))
    print(sort_by_digit_count(list(range(100000))))
