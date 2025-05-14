def count_and_say(n):
    if n == 1:
        return "1"

    curr = "1"

    for i in range(2, n + 1):
        next_seq = []
        cnt = 1

        for j in range(1, len(curr)):
            if curr[j] == curr[j - 1]:
                cnt += 1
            else:
                next_seq.append(str(cnt))
                next_seq.append(curr[j - 1])
                cnt = 1

        next_seq.append(str(cnt))
        next_seq.append(curr[-1])
        curr = ''.join(next_seq)

    return curr
