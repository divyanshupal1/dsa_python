def dice(res, number):
    if number == 0:
        print(res)
    for i in range(1, number + 1):
        dice(res + str(i), number - i)


if __name__ == '__main__':
    dice('', 6)
