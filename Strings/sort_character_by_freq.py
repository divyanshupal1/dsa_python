def frequencySort(s: str) -> str:
    freq = {}
    for i in s:
        if freq.keys().__contains__(i):
            freq[i] += 1
        else:
            freq[i] = 1
    dict_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    res = ""
    for item in dict_sorted:
        res += item[0]*item[1]
    return res


if __name__ == '__main__':
    frequencySort('abbccc')
