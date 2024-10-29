from files.ex01 import value_counts


def add_counters(counter1, counter2):
    result = dict(counter1)
    for k, v in counter2.items():
        result[k] = result.get(k, 0) + v
    return result


def main():
    counter1 = value_counts('brontosaurus')
    counter2 = value_counts('apatosaurus')
    print(add_counters(counter1, counter2))


if __name__ == '__main__':
    main()
