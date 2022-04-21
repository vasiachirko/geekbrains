"""
Вывести на экран букву "W" из символов "*" (звездочка).
"""


def print_line(*pos_of_pixels):
    str_len = 5
    for i in range(1, str_len + 1):
        if i in pos_of_pixels:
            print('* ', end='')
        else:
            print('_ ', end='')
    print()


def print_line2(*pos_of_pixels):
    str_len = 5
    print(' '.join(list(map(lambda x: '*' if x in pos_of_pixels else '_', range(1, str_len + 1)))))


for i in range(3):
    print_line2(1, 5)
print_line2(1, 3, 5)
print_line2(2, 4)
