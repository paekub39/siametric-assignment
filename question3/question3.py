def count_n(byte):
    n = 0
    for bit in byte:
        if bit != "1":
            is_correct_format = 2 <= n <= 4
            return is_correct_format, n
        n = n + 1
    return False, n


def is_it_a_valid_utf_8_encode(data):
    i = 0
    while i < len(data):
        b = format(data[i], "b")
        if len(b) != 8:
            i = i + 1
            continue
        is_correct_format, n = count_n(b)

        if not is_correct_format:
            return False

        if i + n - 1 >= len(data):
            return False

        for j in range(1, n, 1):
            b = format(data[i + j], "b")
            if len(b) != 8:
                return False
            if b[0] != '1' or b[1] != '0':
                return False
        i = i + n

    return True


if __name__ == '__main__':
    data = [197, 130, 1]
    print(is_it_a_valid_utf_8_encode(data))
