def d_search(d, n):
    for k, v in d.items():
        if v == n:
            return k
    return ''


def shift_word(word, number, letters, letter_map):
    result = ''
    for l in word:
        result += d_search(letter_map, (letter_map[l] + number) % len(letter_map))
        # result += letters[(letter_map[l] + number) % len(letter_map)]
    return result


def main():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = range(len(letters))
    zip_list = zip(letters, numbers)
    letter_map = dict(zip_list)
    # print(letter_map)
    print(shift_word('cheer', 7, letters, letter_map))
    print(shift_word('melon', 16, letters, letter_map))


if __name__ == '__main__':
    main()
