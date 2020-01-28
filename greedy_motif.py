
def Pr(Text, Profile):
    pr = 1
    # insert your code here
    for i in range(len(Text)):
        pr = pr*Profile[Text[i]][i]
    return pr
def ProfileMostProbableKmer(text, k, profile):
    pr = {}
    maxp = -1
    most = ""
    kmer = ""
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        p = Pr(kmer, profile)
        pr[kmer] = p
    ma = max(pr.values())
    for key, value in pr.items():
        if(pr[key] == ma):
            return key
def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for m in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][m:m+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs
profile = {}
profile["A"] = [0.4, 0.3, 0.0, 0.1, 0.0, 0.9]
profile["C"] = [0.2, 0.3, 0.0, 0.4, 0.0, 0.1]
profile["G"] = [0.1, 0.3, 1.0, 0.1, 0.5, 0.0]
profile["T"] = [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]
print(Pr("TCGGTA", profile))
