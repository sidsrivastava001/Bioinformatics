def Reverse(Pattern):
    newpatt = ""
    for i in reversed(range(len(Pattern))):
        newpatt+=Pattern[i]
    return newpatt
def Complement(Pattern):
    # your code here
    newpatt = ""
    for i in range(len(Pattern)):
        if(Pattern[i] == 'A'):
            newpatt+='T'
        elif(Pattern[i] == 'C'):
            newpatt+='G'
        elif(Pattern[i] == 'G'):
            newpatt+='C'
        elif(Pattern[i] == 'T'):
            newpatt+='A'
    return newpatt
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    # your code here
    for i in range(len(Genome)-len(Pattern)+1):
        if(Genome[i:i+len(Pattern)] == Pattern):
            positions.append(i)
    return positions
