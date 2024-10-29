import json
import os.path


def load_word_dict(file_path):
    word_dict = {}
    json_file_path = '../file/words.json'
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as json_file:
            word_dict = json.load(json_file)
    with open(file_path, 'r') as word_file:
        for word in word_file:
            word = word.strip().lower()
            word_dict[word] = True
    with open('../file/words.json', 'w') as json_file:
        json.dump(word_dict, json_file, indent=4)
    return word_dict


def is_interlocking(word, word_dict):
    word = word.lower()
    first = word[0::2]
    second = word[1::2]
    return first in word_dict and second in word_dict


# nothing

def main():
    print(is_interlocking('schooled', load_word_dict('../file/words.txt')))


if __name__ == '__main__':
    main()
