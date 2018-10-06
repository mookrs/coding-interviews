def verify_sequence_of_bst(sequence):
    if not sequence:
        return False

    length = len(sequence)
    root = sequence[-1]

    left = 0
    while sequence[left] < root:
        left += 1

    right = left
    while right < length - 1:
        if sequence[right] < root:
            return False
        right += 1

    left_ret = True if left == 0 else verify_sequence_of_bst(sequence[:left])
    right_ret = True if left == right else verify_sequence_of_bst(sequence[left:right])
    return left_ret and right_ret
