def main():
    list0 = [1, 2, 3]
    list1 = [4, 5]

    t = (list0, list1)
    print(t)
    t[1]
    list1.append(6)
    print(t)
    t = (tuple(t[0]), tuple(t[1]))
    print(t)

    d = {t: 'hello world'}
    print(d)


if __name__ == '__main__':
    main()
