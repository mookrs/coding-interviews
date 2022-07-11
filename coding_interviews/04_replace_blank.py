def replace_space(s):
    if not isinstance(s, str) or not s:
        return ""

    space_num = 0
    for i in s:
        if i == " ":
            space_num += 1

    new_str_len = len(s) + space_num * 2
    new_str = new_str_len * [None]
    index_of_original, index_of_new = len(s) - 1, new_str_len - 1
    while index_of_new >= 0 and index_of_new >= index_of_original:
        if s[index_of_original] == " ":
            new_str[index_of_new - 2 : index_of_new + 1] = ["%", "2", "0"]
            index_of_new -= 3
        else:
            new_str[index_of_new] = s[index_of_original]
            index_of_new -= 1
        index_of_original -= 1
    return "".join(new_str)


s = "we are happy"
print(replace_space(s))
