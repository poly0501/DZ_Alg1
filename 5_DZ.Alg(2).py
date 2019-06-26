from collections import deque

BASE = 16
HEX_NUMBERS = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'}
BIN_NUMBERS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}


def sum_hex(left, right):
    left = left.copy()
    right = right.copy()

    if len(right) > len(left):
        left, right = right, left

    right.extendleft("0" * (len(left) - len(right)))

    result = deque()
    overflow = 0
    while len(left) != 0:
        left_num = BIN_NUMBERS[left.pop()]
        right_num = BIN_NUMBERS[right.pop()]

        result_num = left_num + right_num + overflow

        if result_num >= BASE:
            overflow = 1
            result_num -= BASE
        else:
            overflow = 0

        result.appendleft(HEX_NUMBERS[result_num])

    if overflow == 1:
        result.appendleft("1")

    return result


if __name__ == "__main__":
    a = deque(input("Введите первое число в 16-ой с.с.(от 0 до F): ").upper())
    b = deque(input("Введите второе число в 16-ой с.с.(от 0 до F): ").upper())

    print(f'{list(a)} + {list(b)} =  {list(sum_hex(a, b))}')
