def hIndex(citations):
    n = len(citations)
    freq = [0] * (n + 1)

    # count the frequency of citations
    for citation in citations:
        if citation >= n:
            freq[n] += 1
        else:
            freq[citation] += 1

    idx = n

    # variable to keep track of the count of papers
    # having at least idx citations
    s = freq[n]
    while s < idx:
        idx -= 1
        s += freq[idx]

    # return the largest index for which the count of
    # papers with at least idx citations becomes >= idx
    return idx


if __name__ == '__main__':
    citations = [6, 0, 3, 5, 3]
    print(hIndex(citations))