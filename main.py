# Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.
#
# Чтобы записать байты можно использовать список с числами и функцию bytes
from random import choice, randint


def rand_file(extension="txt", letter_min=6, letter_max=30, content_min=0, content_max=15, file_count=42):
    """Функцию, которая создаёт файлы с указанным расширением."""

    for _ in range(file_count):
        # генерирует случайное количество символов от [6 до 30]
        LETTERS = "abcdfjhtuerpqomnaaz"
        word = ''
        for _ in range(randint(letter_min, letter_max)):
            word += choice(LETTERS)

            # Генератор randbytes на моей версии не поддерживается
        content_256_byte = b'\xf8F\xca\xf8\x11\xf1Q\xbc\xe6\xe0\x96\x1b\x17\x8a\xaf\x13V\xd1AMh\xac\xaf?\xe9\\N\xb6u1' \
                           b'\xd0t&\\\x0e\x15\xa0\x98\x8e\x83\xa1\xa5\x8e\x00x\xef\xc9T\x18"K\x07uM3\x8b\xb6\x14\x97t' \
                           b'\xeeI\x90\xaed\xc9\x85\xec\x95\x90\xec\x13v<\x16\xcd\xa2\xf3\xa4\xd5\x03\x13\x835\xec]3\x97' \
                           b'\xfc\xb4j\x12b\xd55h\x0eT\x14\x8a-\x87\xcaj\xd5\xd2\xb2\xce\x16\x01\x0em\xff\xa0\x01\x94' \
                           b'`\xaf\xc7\x1d\x97\xdf\x10\x80\x8b\xa4p\x1d4K/\xc4.\xdf\x01\x8a\x92YN\xf1~\x80$\x90j\xaaQ\xf7' \
                           b'\xcf\x13\x99\xc87&\x1a\xfd*\x16\xabe*\xab\x9a\x9e\xaf\x1baP\x94\xcd\xb2\xf5\x0f\xc7\xfa\xd0' \
                           b'\x93\xdd\x1faVH\\bo\xccC\x8eV\xd3e\xf3\x98\x9b\\ FWR\x12\x84\xcd*{' \
                           b'\x94\xe2]@\xa5@g\x82t\xe6H\x81\xe0\xb4R\xb5\xbe\xb6\xfc@E\xba\xdb\t\xc8\x98\xa6\x8f1\x07\xa4' \
                           b'\xa9c\xf9\xda5\xce\xe8\xdd\xb73p\xb1\xd6\xcd\xe0\xf0C\xa1\x1b\xd2\xae '

        # генерирует случайное количество байт от [256 до 4096]
        for _ in range(randint(content_min, content_max)):
            content_256_byte += content_256_byte

        x = open(word + "." + extension, "wb")
        x.write(content_256_byte)
        x.close()


if __name__ == '__main__':
    rand_file("md", 6, 7, 0, 1, 3)