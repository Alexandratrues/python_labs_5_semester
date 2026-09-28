def swap_long_with_short(text: str, separators: str) -> str:
    if len(text) > 300:
        print("длина строки больше 300 символов")
        return ""

    words_data = []
    n = len(text)
    i = 0
    while i < n:
        if text[i] not in separators:
            start = i
            while i < n and text[i] not in separators:
                i += 1
            end = i
            word = text[start:end]
            words_data.append((word, start, end))
        else:
            i += 1

    if len(words_data) < 2:
        print(f"мало слов")
        return ""

    longest_idx = 0
    shortest_idx = 0

    max_len = len(words_data[0][0])
    min_len = len(words_data[0][0])

    for idx in range(len(words_data)):
        word_len = len(words_data[idx][0])

        if word_len > max_len:
            max_len = word_len
            longest_idx = idx

        if word_len <= min_len:
            min_len = word_len
            shortest_idx = idx

    if min_len == max_len:
        print("слова одной длины")
        return ""

    if longest_idx < shortest_idx:
        first_idx, second_idx = longest_idx, shortest_idx
    else:
        first_idx, second_idx = shortest_idx, longest_idx

    word1, start1, end1 = words_data[first_idx]
    word2, start2, end2 = words_data[second_idx]

    result = (text[:start1] + word2 + text[end1:start2] + word1 + text[end2:])
    return result


def main():
    print("обмен слов")
    
    seps = input("введите разделители: ")
    if not seps:
        seps = " "
        print("по умолчанию: пробел")

    string = input("введите строку (до 300 символов):\n").strip("\r\n")

    transformed = swap_long_with_short(string, seps)
    if transformed:
        print("\nрезультат:")
        print(f"{transformed}")

main()
