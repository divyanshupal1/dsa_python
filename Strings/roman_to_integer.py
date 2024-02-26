def romanToInt(s: str) -> int:
    res = 0
    n = -len(s)

    while n < 0:

        if s[n] == 'I':
            if n != -1 and s[n+1] == 'V':
                res += 4
                n += 2
                continue
            if n != -1 and s[n+1] == 'X':
                res += 9
                n += 2
                continue
            else:
                res += 1

        elif s[n] == 'V':
            res += 5
        elif s[n] == 'X':
            if n != -1 and s[n+1] == 'L':
                res += 40
                n += 2
                continue
            if n != -1 and s[n+1] == 'C':
                res += 90
                n += 2
                continue
            else:
                res += 10
        elif s[n] == 'L':
            res += 50
        elif s[n] == 'C':
            if n != -1 and s[n+1] == 'D':
                res += 400
                n += 2
                continue
            if n != -1 and s[n+1] == 'M':
                res += 900
                n += 2
                continue
            else:
                res += 100
        elif s[n] == 'D':
            res += 500
        elif s[n] == 'M':
            res += 1000
        n += 1
        print(res, n)
    return res


if __name__ == '__main__':
    print(romanToInt('XCII'))
