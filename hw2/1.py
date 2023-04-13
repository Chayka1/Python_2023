from pympler import asizeof


def find_word_in_file(find_word):
    with open('hw2/rockyou.txt', 'r') as file:
        for words in file.readlines():
            if find_word in words.lower():
                with open('hw2/results.txt', 'a') as find_words:
                    find_words.write(words)
    
    with open('hw2/results.txt', 'r') as file:
        num_lines = len(file.readlines())
        print("Количество строк в файле:", num_lines)

    with open('hw2/results.txt', 'rb') as file:
        size = asizeof.asizeof(file.read())
        print("Общий размер файла results.txt:", size, "байт")

if __name__ == "__main__":
    find = input('Введите слово: ')
    find_word_in_file(find)