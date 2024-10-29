def count_value_py(word):
    counter = {}
    for l in word:
        counter[l] = counter.get(l, 0) + 1
    return counter


def count_value(word):
    counter = {}
    for l in word:
        if l in counter:
            counter[l] += 1
        else:
            counter[l] = 1
    return counter


def sort_func(k, v):
    return v


def find_max(d):
    max = 0
    max_k = ''
    for k, v in d.items():
        if v > max:
            max = v
            max_k = k
    return max_k


def my_sorted(d):
    result = []
    for i in range(len(d)):
        max_k = find_max(d)
        result.append(max_k)
        d[max_k] = 0
    return result


def most_frequent_letters(word):
    """print the letters in decreasing frequency."""
    counter = count_value(word)
    # return sorted(counter)
    return sorted(counter, key=lambda k: counter[k], reverse=True)


def main():
    # print(count_value('hello'))
    # print(count_value_py('hello'))
    print(most_frequent_letters('hello'))


if __name__ == '__main__':
    main()
