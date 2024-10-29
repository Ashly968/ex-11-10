from files.ex01 import value_counts


def has_duplicates_v2(word):
    return len(set(word)) != len(word)


def has_duplicates(word):
    return len(value_counts(word).keys()) != len(word)


def main():
    print(has_duplicates('unpredictably'))
    print(has_duplicates('hello'))

    print(has_duplicates_v2('unpredictably'))
    print(has_duplicates_v2('hello'))


if __name__ == '__main__':
    main()
