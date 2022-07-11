def to_string(chars):
    return ''.join(chars)


def my_permutation(s):
    ret = set()

    def permutation(chars, begin):
        if begin == len(chars) - 1:
            ret.add(to_string(chars))
        else:
            for i in range(begin, len(chars)):
                chars[begin], chars[i] = chars[i], chars[begin]
                permutation(chars, begin + 1)
                chars[begin], chars[i] = chars[i], chars[begin]

    permutation(list(s), 0)
    return sorted(list(ret))


s = 'abc'
print(my_permutation(s))
