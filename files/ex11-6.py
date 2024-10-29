#! usr/bin/env python3

def word_distance_py(word1, word2):
    return sum(1 for c1, c2 in zip(word1, word2) if c1 != c2)


def word_distance(word1, word2):
    counter = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            counter += 1
    return counter


def main():
    print(word_distance('latter', 'letter'))
    print(word_distance_py('latter', 'letter'))


if __name__ == '__main__':
    main()
