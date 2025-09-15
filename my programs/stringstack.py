def stringStack(pat, tar):
    i = len(pat) - 1
    j = len(tar) - 1
    while i >= 0 and j >= 0:
        if pat[i] != tar[j]:
            i -= 2  # Simulate the "delete" operation by skipping previous
        else:
            i -= 1
            j -= 1
    return j < 0
