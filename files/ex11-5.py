#!/usr/bin/env python3


def print_anagrams(d):
    for k, v in d.items():
        if len(v) > 1:
            print(v)


def load_word(file_path):
    result = {}
    with open(file_path, 'r') as word_file:
        for word in word_file:
            word = word.strip()
            key = ''.join(sorted(word))
            result.setdefault(key, []).append(word)
    return result

    # if key in result:
    #   result[key] = result[key].append(word)
    # else:
    #   result[key] = [word]


def main():
    # print(load_word('file/words.txt'))
    print_anagrams(load_word('../file/words.txt'))


if __name__ == '__main__':
    main()
