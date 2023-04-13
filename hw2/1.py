from pympler import asizeof


def words_generator(find_word):
    with open('hw2/rockyou.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            elif find_word in line:
                yield line

def find_words_of_generator(find_word):
    with open('hw2/results.txt', 'a') as find_words:
        for item in words_generator(find_word):
            find_words.write(item)
  
def file_info():
    with open('hw2/results.txt', 'r') as file:
        num_lines = len(file.readlines())
        print("Количество строк в файле:", num_lines)

    with open('hw2/results.txt', 'rb') as file:
        size = asizeof.asizeof(file.read())
        print("Общий размер файла results.txt:", size, "байт")


if __name__ == "__main__":
    find = input('Введите слово: ')
    find_words_of_generator(find)
    file_info()
