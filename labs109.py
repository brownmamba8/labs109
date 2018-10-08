def ryerson_letter_grade(pct):
    """
    TODO
    """
    if 0 < pct < 50:
        return 'F'
    elif pct <= 59:
        return 'D'
    elif pct <= 69:
        return 'C'
    elif pct <= 79:
        return 'B'
    elif pct <= 100:
        return 'A'


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


def caps_lock_stuck(text):
    """
    Should work but doesn't pass
    """
    caps_lock = False
    new_text = ''

    for char in text:
        if char.lower() in ['a', 'z']:
            caps_lock = not caps_lock
            continue

        new_text += char.swapcase() if caps_lock else char

    return new_text


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


def contains_bingo(card, numbers, centerfree=True):
    rows = []

    for x in range(5):
        # Diagonals
        h_row = []
        v_row = []

        for y in range(5):
            if x == y == 2 and centerfree:
                continue

            h_row.append(card[x][y])
            v_row.append(card[y][x])

    # Diagonals
    for i in range(5):


    for row in rows:
        if set(row).issubset(numbers):
            return True

    return False


c = [
    [38, 93, 42, 47, 15],
    [90, 13, 41, 10, 56],
    [54, 23, 87, 70, 6],
    [86, 43, 48, 40, 92],
    [71, 24, 44, 1, 34]
]

n = [
    1, 2, 3, 4, 6, 8, 12,
    13, 15, 16, 19, 21, 22,
    24, 28, 34, 38, 40, 41,
    42, 43, 45, 47, 49, 51,
    53, 55, 57, 58, 62, 65,
    66, 69, 70, 72, 82, 83,
    84, 86, 88, 95, 97
]


print(contains_bingo(c, n))