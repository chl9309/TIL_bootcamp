def my_strcmp(word1, word2):
    pass
    # 두 단어중 더 짧은 단어의 길이
    # 두 단어를 idx 기준으로 비교해 나갈건데
        # 만약 두 알파벳이 다르다
            # 두 단어의 ASCII 코드 값의 차를 반환
    # 만약 짧은 단어기준으로 비교했는데 서로 다른 알파벳이 없다면
        # 두 단어의 길이가 같으면 0 반환
        # word1이 더 길면 : 사전 순서상 뒤가 될 테니 1 반환
    if len(word1) != len(word2):
        short = len(word1)
        result = 0
    for i in range(short):

        if word1[i] != word2[i]:
            return abs(ord(word1[i]) - ord(word2[i]))

        else:
            result



def my_



print(my_strcmp('abc', 'abcd'))

print(my_strcmp('Zab', 'zab'))

