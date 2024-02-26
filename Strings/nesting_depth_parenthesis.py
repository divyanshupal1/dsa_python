def maxDepth(s: str) -> int:
    depth, res = 0, 0
    for i in s:
        if i == '(':
            depth += 1
        if i == ')':
            depth -= 1
        res = max(depth, res)
    return res


if __name__ == '__main__':
    print(maxDepth('(((8)))'))
