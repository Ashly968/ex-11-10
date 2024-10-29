from files.ex01 import value_counts


def find_repeats_v2(counter):
    return [k for k, v in counter.items() if v > 1]


def find_repeats(counter):
    result = []
    for k, v in counter.items():
        if v > 1:
            result.append(k)
    return result


def main():
    print(find_repeats(value_counts('brontosaurus')))
    print(find_repeats_v2(value_counts('brontosaurus')))


if __name__ == '__main__':
    main()
