def SkewArray(Genome):
    # your code here
    Skew = [0]
    for i in range(len(Genome)):
        if(Genome[i] == 'A' or Genome[i] == 'T'):
            Skew.append(Skew[i])
        if(Genome[i] == 'G'):
            Skew.append(Skew[i]+1)
        if(Genome[i] == 'C'):
            Skew.append(Skew[i]-1)
    return Skew
def MinimumSkew(Genome):
    positions = [] # output variable
    skew = SkewArray(Genome)
    minarray = min(skew)
    for i in range(len(skew)):
        if(skew[i] == minarray):
            positions.append(i)
    return positions
print(MinimumSkew("CATTCCAGTACTTCGATGATGGCGTGAAGA"))
