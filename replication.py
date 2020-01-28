def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for i in range(n-k+1):
            if(Text[i:i+k] == Pattern):
                   freq[Pattern] = freq[Pattern]+1


    return freq
def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if(freq[key] == m):
            words.append(key)
    return words
x = FrequencyMap("TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT", 3)
print(x)
