def permutations(str):
    if len(str) == 1:
        return str
    result = []
    for ch in range(len(str)):
        without_i_char = str[:ch] + str[ch+1:]
        for permutation in permutations(without_i_char):
            result.append(str[ch] + permutation)

    return result

print(permutations("abc"))


def permutations1(s):
    result = []
    s = list(s)

    def backtrack(start):
        if start == len(s):
            result.append(''.join(s))
            return

        for i in range(start, len(s)):
            s[start], s[i] = s[i], s[start]
            backtrack(start + 1)
            s[start], s[i] = s[i], s[start]

    backtrack(0)
    return result


print(permutations1("abc"))
