def HammingDistance(p, q):
    dist = 0
    for i in range(len(p)):
        if(p[i] != q[i]):
            dist = dist+1
    return dist
def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    # your code here
    positions = [] # initializing list of positions
    for i in range(len(Text)-len(Pattern)+1):
        dist = HammingDistance(Text[i:i+len(Pattern)], Pattern)
        if(dist <= d):
            positions.append(i)
    count = len(positions)
    return count
print(HammingDistance("CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT", "CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG"))
