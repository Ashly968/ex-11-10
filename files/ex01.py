def value_counts(string):
    counter = {}
    for letter in string:
        counter[letter] = counter.get(letter, 0) + 1
    return counter


def main():
    print(value_counts('brontosaurus'))


if __name__ == '__main__':
    main()
